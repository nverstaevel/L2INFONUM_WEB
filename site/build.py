#!/usr/bin/env python3
"""Build the bilingual course site into site/_build.  Usage: python site/build.py"""
import json
import pathlib
import hashlib
import html
import re
import shutil
import subprocess
import zipfile

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = SITE / "_build"
REPO = "https://github.com/nverstaevel/L2INFONUM_WEB"
UI = {
    "en": {"nav": {"index": "Home", "cours": "Lectures", "tds": "Labs", "references": "References", "notions": "Notions", "recipes": "Recipes", "cheatsheets": "Cheat sheets",
                   "setup": "Setup", "troubleshooting": "Troubleshooting", "glossary": "Glossary"},
           "brand": "Web & Open Data", "skip": "Skip to content", "other": ("fr", "Français"), "theme": "Light / dark",
           "bored": "I'm bored", "tag": "L2 Digital Studies & Management", "menu": "Main menu", "crumbs": "You are here",
           "prev": "Previous", "next": "Next", "top": "Back to top", "help": "Help", "all": "All references"},
    "fr": {"nav": {"index": "Accueil", "cours": "Cours", "tds": "TD", "references": "Références", "notions": "Notions", "recipes": "Recettes", "cheatsheets": "Fiches mémo",
                   "setup": "Installation", "troubleshooting": "Dépannage", "glossary": "Glossaire"},
           "brand": "Web et données ouvertes", "skip": "Aller au contenu", "other": ("en", "English"), "theme": "Clair / sombre",
           "bored": "Je m'ennuie", "tag": "L2 Numérique et management", "menu": "Menu principal", "crumbs": "Vous êtes ici",
           "prev": "Précédent", "next": "Suivant", "top": "Haut de page", "help": "Aide", "all": "Toutes les références"},
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


def version(name):
    """Short fingerprint of an asset, so that browsers reload it when it changes."""
    return hashlib.sha1((SITE / "assets" / name).read_bytes()).hexdigest()[:8]


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


HELP = ("cheatsheets", "setup", "troubleshooting", "glossary")
REFS = {"notion-html-tags": "HTML", "notion-css-ref": "CSS", "notion-js-ref": "JavaScript",
        "notion-python-ref": "Python", "notion-flask-ref": "Flask"}


def section(name):
    """Menu entry a page belongs to."""
    if name in REFS:
        return "references"
    for pattern, key in ((r"cm\d+", "cours"), (r"td\d+", "tds"), (r"notion-", "notions"), (r"recipe-", "recipes")):
        if re.match(pattern, name):
            return key
    return name


def link(name, target, label, here=None):
    current = ' aria-current="page"' if target == name else ' aria-current="true"' if target == here else ""
    return f'<a href="{target}.html"{current}>{label}</a>'


def dropdown(label, links, active, extra=""):
    """A menu entry that opens a list of links (works without JavaScript)."""
    current = ' class="current"' if active else ""
    return (f'<details class="drop {extra}"><summary{current}>{label}</summary>'
            f'<div class="panel">{"".join(links)}</div></details>')


def menu(lang, name):
    ui, here = UI[lang], section(name)
    nav = ui["nav"]
    out = [link(name, key, nav[key], here) for key in ("index", "cours", "tds")]
    refs = [link(name, page_name, label) for page_name, label in REFS.items()]
    refs.append(link(name, "references", ui["all"]))
    out.append(dropdown(nav["references"], refs, here == "references"))
    out += [link(name, key, nav[key], here) for key in ("notions", "recipes")]
    helps = [link(name, key, nav[key]) for key in HELP]
    return "".join(out) + dropdown(ui["help"], helps, here in HELP, "help")


def switcher(lang, name):
    """Go from one reference page to another."""
    if name not in REFS:
        return ""
    links = "".join(link(name, page_name, label) for page_name, label in REFS.items())
    return f'<nav class="switch" aria-label="{UI[lang]["nav"]["references"]}">{links}</nav>'


def breadcrumbs(lang, name, title):
    ui, here = UI[lang], section(name)
    if name == "index":
        return ""
    trail = f'<li><a href="index.html">{ui["nav"]["index"]}</a></li>'
    if here != name:
        trail += f'<li><a href="{here}.html">{ui["nav"][here]}</a></li>'
    trail += f'<li aria-current="page">{title}</li>'
    return f'<nav class="crumbs" aria-label="{ui["crumbs"]}"><ol>{trail}</ol></nav>'


def pager(lang, name):
    """Previous and next session, for lectures and labs."""
    found = re.fullmatch(r"(cm|td)(\d+)", name)
    if not found:
        return ""
    kind, number = found.group(1), int(found.group(2))
    ui, out = UI[lang], ""
    for step, key, arrow in ((-1, "prev", "←"), (1, "next", "→")):
        other = f"{kind}{number + step}"
        source = SITE / "content" / lang / f"{other}.md"
        if source.exists():
            title = source.read_text(encoding="utf-8").split("\n", 1)[0].removeprefix("title:").strip()
            out += f'<a class="{key}" href="{other}.html"><small>{arrow} {ui[key]}</small>{title}</a>'
    return f'<nav class="pager">{out}</nav>'


def page(lang, name, title, body, extra_head="", toc=""):
    ui = UI[lang]
    other, other_label = ui["other"]
    fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
             'family=Nunito+Sans:wght@400;600;700;800&display=swap">')
    return f"""<!doctype html>
<html lang="{lang}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>{fonts}<link rel="stylesheet" href="../assets/site.css?v={version('site.css')}">{extra_head}
<script src="../assets/site.js?v={version('site.js')}"></script></head>
<body class="page-{section(name)}" id="top"><a class="skip" href="#content">{ui['skip']}</a>
<header class="masthead"><div class="bar">
<a class="brand" href="index.html">{ui['brand']}<small>{ui['tag']}</small></a>
<div class="actions"><a class="bored" href="bored.html"><span aria-hidden="true">🥱</span> {ui['bored']}</a>
<a href="../{other}/{name}.html" lang="{other}">{other_label}</a><button type="button" id="theme">{ui['theme']}</button></div>
</div></header>
<nav class="menu" aria-label="{ui['menu']}"><div class="bar">{menu(lang, name)}</div></nav>
<div class="{'layout with-toc' if toc else 'layout'}">{toc}
<main id="content">{breadcrumbs(lang, name, title)}<h1>{title}</h1>
{switcher(lang, name)}
{body}
{pager(lang, name)}</main></div>
<a class="to-top" href="#top" hidden>↑ {ui['top']}</a>
<footer>© 2026 Nicolas Verstaevel · Université Toulouse Capitole · <a href="../LICENSE.txt">{LICENCE[lang]}</a> · <a href="{REPO}">GitHub</a></footer>
</body></html>"""


LICENCE = {"en": "MIT licence (third-party data excepted)", "fr": "Licence MIT (hors données tierces)"}
PREVIEW = re.compile(r"notion-flask-ref$|notion-html-|recipe-page-skeleton$|recipe-table-form$")
LABEL = {"en": ("Result in the browser", "links and buttons are inactive here"),
         "fr": ("Résultat dans le navigateur", "liens et boutons inactifs ici")}


def previews(lang, body):
    """Show, under each HTML example, what a browser displays (isolated, no script)."""
    title, note = LABEL[lang]

    def add(match):
        code = html.unescape(match.group(1))
        if "<script" in code or "{{" in code:
            return match.group(0)
        shown = re.sub(r'src="images/[^"]*"', 'src="../assets/demo.svg"', code)
        shown = re.sub(r'<link rel="stylesheet"[^>]*>', "", shown)
        if "<html" not in shown:
            shown = f'<!DOCTYPE html><meta charset="utf-8">{shown}'
        shown = shown.replace('<meta charset="utf-8">', '<meta charset="utf-8"><base target="_blank">', 1)
        return (f'{match.group(0)}<div class="preview"><p><strong>{title}</strong> · {note}</p>'
                f'<iframe sandbox="allow-same-origin" title="{title}" srcdoc="{html.escape(shown)}"></iframe></div>')

    return re.sub(r'<pre><code class="language-html">(.*?)</code></pre>', add, body, flags=re.S)


LABS = ("td1", "td2", "td3", "td4", "td5", "td6", "td7", "project")


def starter_zips():
    """One ZIP of starter files per lab, made from the files tracked by git."""
    (OUT / "files").mkdir()
    for folder in LABS:
        names = subprocess.run(["git", "ls-files", folder], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
        assert any(names), folder
        with zipfile.ZipFile(OUT / "files" / f"{folder}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for name in filter(None, names):
                z.write(ROOT / name, name)
            z.write(ROOT / "LICENSE", f"{folder}/LICENSE")


def download_button(lang, body):
    """Add a download button next to the first link to a starter folder."""
    label = {"en": "Download the starter files (ZIP)", "fr": "Télécharger les fichiers de départ (ZIP)"}[lang]
    found = re.search(rf'<a href="{REPO}/tree/main/(\w+)">', body)
    if not found or found.group(1) not in LABS:
        return body
    button = f'<p><a class="download" href="../files/{found.group(1)}.zip" download>⬇ {label} · {found.group(1)}.zip</a></p>'
    end = body.index("</p>", found.end()) + 4
    return body[:end] + button + body[end:]


def build():
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(SITE / "assets", OUT / "assets")
    for deck in (ROOT / "cours").iterdir():
        (OUT / "assets" / f"{deck.name}.css").write_text(deck_css(deck.name), encoding="utf-8")
    starter_zips()
    shutil.copy(ROOT / "LICENSE", OUT / "LICENSE.txt")
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
            if re.fullmatch(r"td\d+", source.stem):
                body = download_button(lang, body)
            if PREVIEW.match(source.stem):
                body = previews(lang, body)
            extra = ""
            found = re.search(r"<p>\{\{slides:(\w+):(\w+)\}\}</p>", body)
            if found:
                cm, slide_lang = found.groups()
                body = body.replace(found.group(0), slides(cm, slide_lang))
                extra = fonts + f'<link rel="stylesheet" href="../assets/{cm}.css">'
            if source.stem == "bored":
                extra = f'<script src="../assets/game.js?v={version("game.js")}"></script>'
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
