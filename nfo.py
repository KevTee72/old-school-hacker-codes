#!/usr/bin/env python3
"""Make a scene style release NFO for your own project.

    python nfo.py --title "My Cool Tool" --group KT72 "works on my machine" "no cracks needed"
"""
import argparse
import datetime

WIDTH = 56


def row(text=""):
    return "| " + text.ljust(WIDTH - 4) + " |"


def field(name, value):
    dots = "." * max(2, 12 - len(name))
    return row(f"{name} {dots} {value}")


def main():
    p = argparse.ArgumentParser(description="NFO file generator")
    p.add_argument("--title", required=True)
    p.add_argument("--group", default="KT72")
    p.add_argument("--version", default="1.0")
    p.add_argument("--platform", default="Windows / Linux / Mac")
    p.add_argument("--date", default=datetime.date.today().isoformat())
    p.add_argument("notes", nargs="*", help="free text lines for the notes section")
    a = p.parse_args()

    border = "+" + "=" * (WIDTH - 2) + "+"
    spaced = " ".join(a.title.upper())
    lines = [
        border,
        row(),
        row(":: " + spaced[:WIDTH - 10] + " ::"),
        row(),
        border,
        field("Group", a.group),
        field("Version", a.version),
        field("Platform", a.platform),
        field("Date", a.date),
        field("Protection", "none, it is open"),
        border,
        row("N O T E S"),
        row(),
    ]
    lines += [row("* " + n) for n in a.notes] or [row("* have fun")]
    lines += [row(), row("Greetings to everyone who ever stayed up all night"),
              row("compiling a kernel."), border]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
