#!/usr/bin/env python3
"""Build the bilingual course site into site/_build.  Usage: python site/build.py"""
import json
import pathlib
import re
import shutil

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = SITE / "_build"
REPO = "https://github.com/nverstaevel/L2INFONUM_WEB"
UI = {
    "en": {"nav": {"index": "Home", "cours": "Lectures", "tds": "Labs", "cheatsheets": "Cheat sheets",
                   "setup": "Setup", "troubleshooting": "Troubleshooting", "glossary": "Glossary"},
           "brand": "Web & Open Data", "skip": "Skip to content", "other": ("fr", "Français"), "theme": "Light / dark"},
    "fr": {"nav": {"index": "Accueil", "cours": "Cours", "tds": "TD", "cheatsheets": "Fiches mémo",
                   "setup": "Installation", "troubleshooting": "Dépannage", "glossary": "Glossaire"},
           "brand": "Web et données ouvertes", "skip": "Aller au contenu", "other": ("en", "English"), "theme": "Clair / sombre"},
}


def slides(cm, lang):
    """Return the slides of one lecture in one language, as scaled frames."""
    deck = ROOT / "cours" / cm
    order = json.loads((deck / "deck.json").read_text(encoding="utf-8"))["order"]
    parts = []
    for slide_id in order:
        if slide_id.startswith(lang + "-"):
            section = (deck / "slides" / f"{slide_id}.html").read_text(encoding="utf-8")
            parts.append(f'<div class="frame">{section.strip()}</div>')
    return '<div class="deck">' + "".join(parts) + "</div>"


def deck_css(cm):
    """Limit the slide stylesheet to the slide frames."""
    css = (ROOT / "cours" / cm / "deck.css").read_text(encoding="utf-8")
    rules = []
    for selectors, body in re.findall(r"([^{}]+)\{([^}]*)\}", css):
        scoped = []
        for s in selectors.strip().split(","):
            s = s.strip()
            scoped.append(f".frame>{s}" if s.startswith(("section", ".cover")) else f".frame {s}")
        rules.append(",".join(scoped) + "{" + body + "}")
    return "\n".join(rules)


def sidebar(lang, tokens):
    """Left menu listing the h2 and h3 sections of a page (none if fewer than two)."""
    def items(entries):
        out = ""
        for e in entries:
            below = items(e["children"]) if e["children"] else ""
            out += f'<li><a href="#{e["id"]}">{e["name"]}</a>{below}</li>'
        return f"<ul>{out}</ul>"
    if len(tokens) < 2:
        return ""
    label = {"en": "On this page", "fr": "Sur cette page"}[lang]
    return (f'<nav class="toc" aria-label="{label}"><details open><summary>{label}</summary>'
            f'{items(tokens)}</details></nav>')


def page(lang, name, title, body, extra_head="", toc=""):
    ui = UI[lang]
    links = "".join(f'<a href="{key}.html">{label}</a>' for key, label in ui["nav"].items())
    other, other_label = ui["other"]
    return f"""<!doctype html>
<html lang="{lang}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="../assets/site.css">{extra_head}
<script src="../assets/site.js"></script></head>
<body><a class="skip" href="#content">{ui['skip']}</a>
<header><nav><a class="brand" href="index.html">{ui['brand']}</a>{links}
<a href="../{other}/{name}.html" lang="{other}">{other_label}</a><button id="theme">{ui['theme']}</button></nav></header>
<div class="{'layout with-toc' if toc else 'layout'}">{toc}
<main id="content"><h1>{title}</h1>
{body}
</main></div>
<footer>Nicolas Verstaevel · Université Toulouse Capitole · <a href="{REPO}">GitHub</a></footer>
</body></html>"""


def build():
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(SITE / "assets", OUT / "assets")
    for deck in (ROOT / "cours").iterdir():
        (OUT / "assets" / f"{deck.name}.css").write_text(deck_css(deck.name), encoding="utf-8")
    fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700'
             '&family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap">')
    for lang in UI:
        (OUT / lang).mkdir()
        for source in sorted((SITE / "content" / lang).glob("*.md")):
            head, text = source.read_text(encoding="utf-8").split("\n---\n", 1)
            title = head.removeprefix("title:").strip()
            md = markdown.Markdown(extensions=["tables", "fenced_code", "md_in_html", "toc"],
                                   extension_configs={"toc": {"toc_depth": "2-3"}})
            body = md.convert(text)
            body = body.replace("[ ]", '<input type="checkbox" aria-label="done">')
            body = body.replace("<table>", '<div class="table"><table>').replace("</table>", "</table></div>")
            extra = ""
            found = re.search(r"<p>\{\{slides:(\w+):(\w+)\}\}</p>", body)
            if found:
                cm, slide_lang = found.groups()
                body = body.replace(found.group(0), slides(cm, slide_lang))
                extra = fonts + f'<link rel="stylesheet" href="../assets/{cm}.css">'
            (OUT / lang / f"{source.stem}.html").write_text(page(lang, source.stem, title, body, extra, sidebar(lang, md.toc_tokens)), encoding="utf-8")
        for pdf in (ROOT / "cours").glob(f"*/*-{lang}.pdf"):
            shutil.copy(pdf, OUT / lang / pdf.name)
    (OUT / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Web &amp; Open Data</title>'
        '<p><a href="en/index.html">English</a> · <a href="fr/index.html">Français</a></p>'
        '<script>location.replace((navigator.language.startsWith("fr") ? "fr" : "en") + "/index.html")</script>',
        encoding="utf-8")


if __name__ == "__main__":
    build()
    print("Built", OUT)
