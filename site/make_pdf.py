#!/usr/bin/env python3
"""Make one PDF per lecture and language with headless Chrome (one slide per page)."""
import pathlib
import subprocess
import sys
import tempfile

from build import ROOT, deck_css, slides

CHROME = sys.argv[1] if len(sys.argv) > 1 else "google-chrome"

for deck in sorted((ROOT / "cours").iterdir()):
    for lang in ("en", "fr"):
        style = ("@page{size:1920px 1080px;margin:0}body{margin:0;-webkit-print-color-adjust:exact}"
                 "table{border-collapse:collapse}.frame{width:1920px;height:1080px;overflow:hidden;break-after:page}"
                 ".frame>section{width:1920px;height:1080px;box-sizing:border-box}" + deck_css(deck.name))
        fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700'
                 '&family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap">')
        page = f'<!doctype html><meta charset="utf-8">{fonts}<style>{style}</style>{slides(deck.name, lang)}'
        with tempfile.TemporaryDirectory() as tmp:
            source = pathlib.Path(tmp) / "deck.html"
            source.write_text(page.replace('class="deck"', ""), encoding="utf-8")
            target = deck / f"{deck.name}-{lang}.pdf"
            subprocess.run([CHROME, "--headless", "--no-sandbox", "--no-pdf-header-footer",
                            f"--print-to-pdf={target}", source.as_uri()], check=True, capture_output=True)
            print("Wrote", target.name)
