#!/usr/bin/env python3
"""Spell words in hexspeak, the way programmers wrote 0xDEADBEEF.

    python hexspeak.py deadbeef cafe babe
    python hexspeak.py "good coffee" facade
    python hexspeak.py --leet "bad code"

Plain mode only accepts words made of the letters a to f. With --leet it also
swaps look alike letters for digits first: o to 0, i and l to 1, s to 5,
t to 7, g to 6, z to 2.
"""
import argparse

LEET = str.maketrans({"o": "0", "i": "1", "l": "1", "s": "5", "t": "7", "g": "6", "z": "2"})
HEX = set("0123456789abcdef")


def spell(word, leet=False):
    w = word.lower().replace(" ", "")
    if leet:
        w = w.translate(LEET)
    if w and set(w) <= HEX:
        return "0x" + w.upper()
    return None


def main():
    p = argparse.ArgumentParser(description="Hexspeak converter")
    p.add_argument("words", nargs="+")
    p.add_argument("--leet", action="store_true", help="swap look alike letters for digits first")
    args = p.parse_args()
    for word in args.words:
        out = spell(word, args.leet)
        bits = f"  ({len(out) - 2 if out else 0} hex digits)" if out else ""
        print(f"{word:<14} -> {out or 'not spellable in hex'}{bits}")


if __name__ == "__main__":
    main()
