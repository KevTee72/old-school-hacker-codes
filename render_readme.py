#!/usr/bin/env python3
"""Regenerate the catalog tables in README.md from codes.json.

    python render_readme.py          rewrite README.md
    python render_readme.py --check  exit 1 if README.md is out of date
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
START, END = "<!-- CATALOG:START -->", "<!-- CATALOG:END -->"


def cell(text):
    return text.replace("|", "\\|")


def build():
    db = json.loads((HERE / "codes.json").read_text(encoding="utf-8"))
    out = []
    for key, title in db["categories"].items():
        rows = [e for e in db["entries"] if e["category"] == key]
        if not rows:
            continue
        out += [f"### {title}", "", "| Code | What it is | Era | Sources |", "|---|---|---|---|"]
        for e in rows:
            links = " ".join(f"[{i}]({u})" for i, u in enumerate(e["sources"], 1))
            out.append(f"| `{cell(e['code'])}` | **{cell(e['title'])}.** {cell(e['what'])} | {cell(e['era'])} | {links} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    readme = HERE / "README.md"
    text = readme.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{START}\n{build()}{END}{tail}"
    if "--check" in sys.argv:
        if new != text:
            print("README.md is out of date, run: python render_readme.py")
            sys.exit(1)
        print("README.md is up to date")
        return
    readme.write_text(new, encoding="utf-8", newline="\n")
    print("README.md updated")


if __name__ == "__main__":
    main()
