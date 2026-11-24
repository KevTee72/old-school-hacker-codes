#!/usr/bin/env python3
"""A fake hacking screen straight out of a 2001 movie.

Nothing here touches the network or any file. It only prints.

    python hollywood.py
    python hollywood.py --target mainframe.local --fast
"""
import argparse
import random
import sys
import time

STEPS = [
    "Resolving target host",
    "Probing open ports",
    "Fingerprinting operating system",
    "Loading exploit module",
    "Bruteforcing login",
    "Escalating privileges",
    "Downloading the secret files",
    "Covering tracks",
]


def hexline():
    addr = random.randint(0, 0xFFFFFF)
    data = " ".join(f"{random.randint(0, 255):02x}" for _ in range(16))
    text = "".join(chr(random.randint(33, 126)) for _ in range(16))
    return f"{addr:08x}  {data}  |{text}|"


def bar(label, speed):
    width = 30
    for i in range(width + 1):
        sys.stdout.write(f"\r{label:<34} [{'#' * i}{'.' * (width - i)}]")
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.06) * speed)
    sys.stdout.write("  OK\n")


def main():
    p = argparse.ArgumentParser(description="Fake hacking screen")
    p.add_argument("--target", default="mainframe.local")
    p.add_argument("--fast", action="store_true")
    args = p.parse_args()
    speed = 0.3 if args.fast else 1.0

    print(f"[*] Target locked: {args.target}")
    print(f"[*] Source IP: 10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}")
    print()
    for step in STEPS:
        bar(step, speed)
    print()
    for _ in range(int(25 * (0.4 if args.fast else 1))):
        print(hexline())
        time.sleep(0.04 * speed)
    print()
    print("*" * 40)
    print("*          ACCESS GRANTED              *")
    print("*" * 40)
    print("(none of that was real, you are safe)")


if __name__ == "__main__":
    main()
