# Retro Hacker Scripts

A small pile of Python scripts for anyone who remembers dial up, IRC, release NFO files and BIOS screens that counted your RAM out loud. Seven small programs, zero dependencies, and not one of them does anything dangerous.

Inspired by the "based on a true story" energy of [NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts), which is worth a read if you have not seen it.

## The scripts

| Script | What it does |
|---|---|
| `matrix.py` | Green digital rain that fills your terminal |
| `hollywood.py` | A fake hacking screen with progress bars, hex dumps and a big ACCESS GRANTED |
| `bios.py` | A fake 2003 BIOS boot screen with the memory counter and IDE detection |
| `leet.py` | Turns plain text into 1337 5p34k in three levels of ridiculousness |
| `dtmf.py` | Writes touch tone phone sounds to a WAV file, and decodes them back |
| `cipher.py` | Caesar, ROT13, Atbash and Vigenere, plus a Caesar brute forcer |
| `nfo.py` | Generates a scene style release NFO for your own projects |

## Quick start

You need Python 3.8 or newer. Nothing to install.

```bash
git clone https://github.com/KevTee72/retro-hacker-scripts.git
cd retro-hacker-scripts
python matrix.py
```

Press Ctrl+C to leave the rain.

## Usage

### matrix.py

```bash
python matrix.py
python matrix.py --seconds 10 --ascii
```

Use `--ascii` if your terminal cannot draw katakana.

### hollywood.py

```bash
python hollywood.py --target mainframe.local
python hollywood.py --fast
```

It only prints. No network, no files. Run it on a second monitor and look busy.

### bios.py

```bash
python bios.py
```

Counts to 512 MB of "memory", detects two drives and pretends to boot Windows 98.

### leet.py

```bash
python leet.py "elite hacker"
python leet.py --level 3 --caps "you have been pwned"
echo "hello world" | python leet.py
```

Output from the first command:

```
31173 h4ck3r
```

Level 1 swaps a few vowels, level 2 adds more letters, and level 3 builds letters out of punctuation like `|-|` for H.

### dtmf.py

```bash
python dtmf.py encode 555-0199 -o call.wav
python dtmf.py decode call.wav
```

Every key on a phone pad is two sine waves played together, one for the row and one for the column. An old telephone exchange listened for exactly that pair. The decoder uses the Goertzel algorithm, which is a cheap way to ask "how much of this one frequency is in the signal" without running a full FFT. Round trip test: encoding `555-0199` and decoding the file gives back `5550199`.

### cipher.py

```bash
python cipher.py rot13 "Hello"
python cipher.py caesar -s 3 "attack at dawn"
python cipher.py caesar -s 3 -d "dwwdfn dw gdzq"
python cipher.py atbash "secret"
python cipher.py vigenere -k LEMON "attack at dawn"
python cipher.py brute "khoor zruog"
```

These are puzzle book ciphers. They protect nothing, so do not use them for anything you care about.

### nfo.py

```bash
python nfo.py --title "My Cool Tool" --group KT72 "works on my machine" "no cracks needed"
```

Prints a boxed release NFO with dotted leader fields, the format scene groups attached to every release in the 2000s. Redirect it into `release.nfo` and ship it with your next side project.

## Why this exists

Early internet culture had a look. Black terminals, green text, spaced out titles, greetings to people you never met. These scripts are a small love letter to that look. They are for fun, for screenshots, for teaching a friend what a Caesar shift is, and for making a demo terminal look like it is doing something important.

## Safety note

Nothing in this repo scans, attacks, intercepts or changes anything on another machine. The "hacking" is theater. The ciphers are for learning. The phone tones are only audio files.

## Contributing

Pull requests with more retro scripts are welcome. Keep them standard library only and keep them harmless. Ideas: a fake dial up modem handshake, a BBS menu, an IRC chat log generator, a defrag screen with blocks that fill in.

## License

MIT. See [LICENSE](LICENSE).
