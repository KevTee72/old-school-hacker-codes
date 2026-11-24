#!/usr/bin/env python3
"""Touch tone dialing sounds. Write a number to a WAV file, or decode one back.

    python dtmf.py encode 555-0199 -o call.wav
    python dtmf.py decode call.wav

Every key on a phone pad is two sine waves played together, one for the row
and one for the column. That pair is what a telephone exchange listened for.
"""
import argparse
import math
import struct
import wave

RATE = 8000
ROWS = [697, 770, 852, 941]
COLS = [1209, 1336, 1477, 1633]
KEYS = ["123A", "456B", "789C", "*0#D"]
FREQ = {k: (ROWS[r], COLS[c]) for r, row in enumerate(KEYS) for c, k in enumerate(row)}


def encode(digits, path, tone=0.1, gap=0.05):
    frames = bytearray()
    for ch in digits.upper():
        if ch not in FREQ:
            continue  # skip spaces and dashes
        lo, hi = FREQ[ch]
        for n in range(int(RATE * tone)):
            v = 0.5 * (math.sin(2 * math.pi * lo * n / RATE) + math.sin(2 * math.pi * hi * n / RATE))
            frames += struct.pack("<h", int(v * 0.8 * 32767))
        frames += b"\x00\x00" * int(RATE * gap)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(bytes(frames))


def goertzel(samples, freq, rate):
    k = 2 * math.cos(2 * math.pi * freq / rate)
    s1 = s2 = 0.0
    for x in samples:
        s0 = x + k * s1 - s2
        s2, s1 = s1, s0
    return s1 * s1 + s2 * s2 - k * s1 * s2


def decode(path):
    with wave.open(path, "rb") as w:
        rate = w.getframerate()
        raw = w.readframes(w.getnframes())
    samples = [v / 32768 for v in struct.unpack(f"<{len(raw) // 2}h", raw)]
    size = int(rate * 0.025)
    result = []
    prev_active = False
    for i in range(0, len(samples) - size + 1, size):
        win = samples[i:i + size]
        energy = sum(x * x for x in win)
        if energy < 1e-6:
            prev_active = False
            continue
        rp = [goertzel(win, f, rate) for f in ROWS]
        cp = [goertzel(win, f, rate) for f in COLS]
        strength = (max(rp) + max(cp)) / (energy * size)
        if strength > 0.3:
            if not prev_active:
                result.append(KEYS[rp.index(max(rp))][cp.index(max(cp))])
            prev_active = True
        else:
            prev_active = False
    return "".join(result)


def main():
    p = argparse.ArgumentParser(description="DTMF encoder and decoder")
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("encode")
    e.add_argument("digits")
    e.add_argument("-o", "--out", default="dial.wav")
    d = sub.add_parser("decode")
    d.add_argument("wav")
    args = p.parse_args()
    if args.cmd == "encode":
        encode(args.digits, args.out)
        print(f"wrote {args.out}")
    else:
        print(decode(args.wav))


if __name__ == "__main__":
    main()
