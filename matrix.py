#!/usr/bin/env python3
"""Digital rain for your terminal. Ctrl+C to quit.

    python matrix.py
    python matrix.py --seconds 10 --ascii
"""
import argparse
import os
import random
import shutil
import sys
import time

KATAKANA = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"
ASCII = "0123456789abcdefghijklmnopqrstuvwxyz@#$%&*+=<>"


def main():
    p = argparse.ArgumentParser(description="Matrix style digital rain")
    p.add_argument("--seconds", type=float, default=0, help="stop after N seconds (0 = forever)")
    p.add_argument("--delay", type=float, default=0.05, help="seconds per frame")
    p.add_argument("--ascii", action="store_true", help="plain ASCII glyphs instead of katakana")
    args = p.parse_args()

    os.system("")  # switches on ANSI escape codes in older Windows consoles
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        args.ascii = True
    glyphs = ASCII if args.ascii else KATAKANA

    cols, rows = shutil.get_terminal_size()
    cols, rows = cols - 1, rows - 1
    heads = [random.randint(-rows, 0) for _ in range(cols)]
    lens = [random.randint(6, max(7, rows)) for _ in range(cols)]
    end = time.time() + args.seconds if args.seconds else None

    sys.stdout.write("\x1b[2J\x1b[?25l")
    try:
        while end is None or time.time() < end:
            out = []
            for x in range(cols):
                y = heads[x]
                if 1 <= y <= rows:
                    out.append(f"\x1b[{y};{x + 1}H\x1b[97m{random.choice(glyphs)}")
                if 1 <= y - 1 <= rows:
                    out.append(f"\x1b[{y - 1};{x + 1}H\x1b[32m{random.choice(glyphs)}")
                tail = y - lens[x]
                if 1 <= tail <= rows:
                    out.append(f"\x1b[{tail};{x + 1}H ")
                heads[x] += 1
                if tail > rows:
                    heads[x] = random.randint(-10, 0)
                    lens[x] = random.randint(6, max(7, rows))
            sys.stdout.write("".join(out))
            sys.stdout.flush()
            time.sleep(args.delay)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\x1b[0m\x1b[?25h\x1b[2J\x1b[H")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
