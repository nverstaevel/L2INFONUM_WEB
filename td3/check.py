"""TD3: check your stylesheet. Run `python check.py` from the td3 folder. Do not modify this file."""
import re
from pathlib import Path


def rules(css, narrow=False):
    """Return {selector: {property: value}} for the normal rules, or for the @media rules."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    media = re.compile(r"@media[^{]*max-width[^{]*\{((?:[^{}]*\{[^{}]*\})*)\s*\}", re.S)
    css = "".join(media.findall(css)) if narrow else media.sub("", css)
    found = {}
    for selectors, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        props = dict((k.strip().lower(), v.strip().lower())
                     for k, v in (line.split(":", 1) for line in body.split(";") if ":" in line))
        for selector in selectors.split(","):
            found.setdefault(" ".join(selector.split()), {}).update(props)
    return found


CSS = Path("style.css").read_text(encoding="utf-8")
R = rules(CSS)
N = rules(CSS, narrow=True)


def has(selector, *names, table=None):
    props = (R if table is None else table).get(selector, {})
    # "a|b" means that one of the two is enough
    return all(any(n in props for n in name.split("|")) for name in names)


def check(name, test):
    try:
        ok = test()
    except Exception as error:  # show the problem and go on with the next check
        print(f"[  ] {name}  ->  {type(error).__name__}: {error}")
        return
    print(f"[OK] {name}" if ok else f"[  ] {name}")


check("1  index.html is here and linked to style.css",
      lambda: bool(re.search(r"<link[^>]*style\.css", Path("index.html").read_text(encoding="utf-8"))))
check("2A body: font-family, color, background",
      lambda: has("body", "font-family", "color", "background|background-color"))
check("2B header: background and padding", lambda: has("header", "background|background-color", "padding"))
check("3A main: max-width, centred, padding",
      lambda: has("main", "max-width", "padding") and "auto" in R["main"].get("margin", "") + R["main"].get("margin-inline", ""))
check("3B img: max-width", lambda: has("img", "max-width"))
check("3C class, id and three colour rules",
      lambda: all(has(sel, "color") for sel in ("p", ".note", "#source"))
      and all(t in Path("index.html").read_text(encoding="utf-8") for t in ('class="note"', 'id="source"')))
check("3D box of .note: width, padding, border, box-sizing, and your result",
      lambda: has(".note", "width", "padding", "border", "box-sizing") and "340" in CSS)
check("4A nav ul: flex, gap, no bullets",
      lambda: R["nav ul"]["display"] == "flex" and has("nav ul", "gap") and "none" in R["nav ul"].get("list-style", ""))
check("4B nav a: color", lambda: has("nav a", "color"))
check("5A table: border-collapse", lambda: R["table"]["border-collapse"] == "collapse")
check("5B th and td: border, padding; th: background",
      lambda: has("th", "border", "padding", "background|background-color") and has("td", "border", "padding"))
check("6A media query: column on narrow screens",
      lambda: N["nav ul"]["flex-direction"] == "column")
