#!/usr/bin/env python3
"""A fake 2003 era BIOS boot screen. Prints only, touches nothing.

    python bios.py
    python bios.py --fast
"""
import argparse
import sys
import time


def main():
    p = argparse.ArgumentParser(description="Fake BIOS POST screen")
    p.add_argument("--fast", action="store_true")
    args = p.parse_args()
    s = 0.15 if args.fast else 1.0

    def line(text="", pause=0.2):
        print(text)
        time.sleep(pause * s)

    line("Award Modular BIOS v6.00PG, An Energy Star Ally", 0.3)
    line("Copyright (C) 1984-2003, Award Software, Inc.", 0.3)
    line()
    line("Pentium(R) 4 CPU 2.40GHz", 0.4)
    line()

    for kb in range(0, 524289, 16384):
        sys.stdout.write(f"\rMemory Test : {kb}K")
        sys.stdout.flush()
        time.sleep(0.02 * s)
    sys.stdout.write("\rMemory Test : 524288K OK\n")
    time.sleep(0.4 * s)
    line()
    line("Detecting IDE Primary Master   ... WDC WD800BB-00CAA1", 0.5)
    line("Detecting IDE Primary Slave    ... None", 0.4)
    line("Detecting IDE Secondary Master ... CD-W524E", 0.5)
    line("Detecting IDE Secondary Slave  ... None", 0.4)
    line()
    line("Press DEL to enter SETUP, ESC to skip memory test", 0.8)
    line()
    line("Verifying DMI Pool Data ........", 0.6)
    line("Boot from CD :", 0.8)
    line("Boot from HDD ...", 0.6)
    line()
    line("Starting Windows 98...", 0.5)
    print("(it is not 2003 anymore, nothing was booted)")


if __name__ == "__main__":
    main()
