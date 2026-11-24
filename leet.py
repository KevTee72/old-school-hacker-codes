#!/usr/bin/env python3
"""Translate plain text into 1337 5p34k, the way chat rooms did it.

    python leet.py "elite hacker"
    python leet.py --level 3 --caps "you have been pwned"
    echo "hello world" | python leet.py
"""
import argparse
import sys

LEVEL1 = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7"}
LEVEL2 = {**LEVEL1, "b": "8", "g": "9", "l": "1", "z": "2"}
LEVEL3 = {
    **LEVEL2,
    "a": "@", "c": "(", "d": "|)", "h": "|-|", "k": "|<",
    "m": "|\\/|", "n": "|\\|", "p": "|>", "u": "|_|", "v": "\\/",
    "w": "\\/\\/", "x": "><", "y": "`/",
}
LEVELS = {1: LEVEL1, 2: LEVEL2, 3: LEVEL3}


def leet(text, level=2, caps=False):
    table = LEVELS[level]
    out = []
    n = 0
    for ch in text:
        low = ch.lower()
        if low in table:
            out.append(table[low])
        elif ch.isalpha():
            out.append(ch.upper() if caps and n % 2 else ch.lower() if caps else ch)
        else:
            out.append(ch)
        if ch.isalpha():
            n += 1
    return "".join(out)


def main():
    p = argparse.ArgumentParser(description="Leetspeak translator")
    p.add_argument("text", nargs="*", help="text to translate, or pipe it in")
    p.add_argument("--level", type=int, choices=[1, 2, 3], default=2)
    p.add_argument("--caps", action="store_true", help="aLtErNaTiNg cAsE on letters left alone")
    args = p.parse_args()
    text = " ".join(args.text) if args.text else sys.stdin.read().rstrip("\n")
    print(leet(text, args.level, args.caps))


if __name__ == "__main__":
    main()
