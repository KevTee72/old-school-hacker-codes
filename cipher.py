#!/usr/bin/env python3
"""Pencil and paper ciphers, the kind from every puzzle book and CTF warmup.

    python cipher.py rot13 "Hello"
    python cipher.py caesar -s 3 "attack at dawn"
    python cipher.py caesar -s 3 -d "dwwdfn dw gdzq"
    python cipher.py atbash "secret"
    python cipher.py vigenere -k LEMON "attack at dawn"
    python cipher.py brute "khoor zruog"

These are toys. None of them protect anything.
"""
import argparse
import sys


def shift(text, n):
    out = []
    for c in text:
        if c.isascii() and c.isalpha():
            base = 65 if c.isupper() else 97
            out.append(chr((ord(c) - base + n) % 26 + base))
        else:
            out.append(c)
    return "".join(out)


def atbash(text):
    out = []
    for c in text:
        if c.isascii() and c.isalpha():
            base = 65 if c.isupper() else 97
            out.append(chr(base + 25 - (ord(c) - base)))
        else:
            out.append(c)
    return "".join(out)


def vigenere(text, key, decode=False):
    ks = [ord(k.lower()) - 97 for k in key if k.isascii() and k.isalpha()]
    if not ks:
        raise SystemExit("key must contain at least one letter")
    out, i = [], 0
    for c in text:
        if c.isascii() and c.isalpha():
            s = -ks[i % len(ks)] if decode else ks[i % len(ks)]
            out.append(shift(c, s))
            i += 1
        else:
            out.append(c)
    return "".join(out)


def main():
    p = argparse.ArgumentParser(description="Classic ciphers")
    p.add_argument("method", choices=["caesar", "rot13", "atbash", "vigenere", "brute"])
    p.add_argument("text", nargs="*")
    p.add_argument("-s", "--shift", type=int, default=3)
    p.add_argument("-k", "--key", default="KEY")
    p.add_argument("-d", "--decode", action="store_true")
    a = p.parse_args()
    text = " ".join(a.text) if a.text else sys.stdin.read().rstrip("\n")

    if a.method == "rot13":
        print(shift(text, 13))
    elif a.method == "caesar":
        print(shift(text, -a.shift if a.decode else a.shift))
    elif a.method == "atbash":
        print(atbash(text))
    elif a.method == "vigenere":
        print(vigenere(text, a.key, a.decode))
    else:
        for n in range(1, 26):
            print(f"{n:>2}  {shift(text, -n)}")


if __name__ == "__main__":
    main()
