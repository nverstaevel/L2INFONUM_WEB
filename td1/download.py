"""TD1, step 2: download the Eurostat dataset tin00028 (internet use by individuals)."""
import gzip
from pathlib import Path

import requests

URL = ""  # TODO 2A: paste the address given in the lab sheet
OUTPUT = Path("data/internet_use.csv")

response = requests.get(URL, timeout=60)
# TODO 2B: stop the script if the status code is not 200

content = response.content
if content[:2] == b"\x1f\x8b":  # provided: unzip if the server sent a compressed file
    content = gzip.decompress(content)

OUTPUT.parent.mkdir(exist_ok=True)
# TODO 2C: write `content` (bytes) into OUTPUT, then print a message
