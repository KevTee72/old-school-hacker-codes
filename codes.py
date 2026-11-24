#!/usr/bin/env python3
"""Look things up in the hacker codes catalog (codes.json).

    python codes.py categories
    python codes.py list
    python codes.py list --category games
    python codes.py search konami
    python codes.py show 2600hz
    python codes.py random
"""
import argparse
import json
import random
import sys
import textwrap
from pathlib import Path

DATA = Path(__file__).with_name("codes.json")


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))


def show(entry, cats):
    print(f"[{cats[entry['category']]}]  {entry['title']}")
    print(f"  code   : {entry['code']}")
    print(f"  era    : {entry['era']}")
    print(textwrap.fill(entry["what"], 78, initial_indent="  ", subsequent_indent="  "))
    for url in entry["sources"]:
        print(f"  source : {url}")
    print()


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="Hacker codes catalog")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("categories")
    ls = sub.add_parser("list")
    ls.add_argument("--category")
    se = sub.add_parser("search")
    se.add_argument("term")
    sh = sub.add_parser("show")
    sh.add_argument("id")
    sub.add_parser("random")
    args = p.parse_args()

    db = load()
    cats, entries = db["categories"], db["entries"]

    if args.cmd == "categories":
        for key, title in cats.items():
            n = sum(1 for e in entries if e["category"] == key)
            print(f"{key:<10} {n:>2}  {title}")
    elif args.cmd == "list":
        for e in entries:
            if args.category and e["category"] != args.category:
                continue
            print(f"{e['id']:<16} {e['code']}")
    elif args.cmd == "search":
        term = args.term.lower()
        hits = [e for e in entries if term in json.dumps(e).lower()]
        for e in hits:
            show(e, cats)
        if not hits:
            print("nothing found")
            sys.exit(1)
    elif args.cmd == "show":
        match = [e for e in entries if e["id"] == args.id]
        if not match:
            sys.exit(f"no entry with id {args.id}, try: python codes.py list")
        show(match[0], cats)
    else:
        show(random.choice(entries), cats)


if __name__ == "__main__":
    main()
