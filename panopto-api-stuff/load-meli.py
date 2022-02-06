import os
import base64


def add(fname, content: str):
    lines = content.splitlines()[4:]

for f in os.listdir():
    if f.startswith("b'") and f.endswith("'.txt"):
        name = base64.b64decode(f[2:-5]).decode("utf-8")
        with open(f) as f:
            c = f.read()
        add(f, c)