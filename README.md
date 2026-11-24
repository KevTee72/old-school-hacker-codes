# Old School Hacker Codes

Real codes, tones, commands and slang from the early hacker and phreaker era, each one checked against a source. Cap'n Crunch whistles, modem AT commands, the Linux SysRq rescue sequence, Konami and Doom cheats, hexspeak numbers, Jargon File slang and the texts people passed around on BBSes.

Inspired by the "based on a true story" energy of [NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts), but this one collects the real artifacts of the culture instead of jokes.

## Try it

You need Python 3.8 or newer. Nothing to install.

```bash
git clone https://github.com/KevTee72/old-school-hacker-codes.git
cd old-school-hacker-codes
python codes.py random
python codes.py search konami
python codes.py list --category phreaking
```

Two things from the catalog you can run right now:

```bash
telnet towel.blinkenlights.nl
```

That plays Star Wars as ASCII art. It answered on port 23 on 2026-11-24. Windows needs the Telnet Client feature turned on first.

```bash
python dtmf.py encode 555-0199 -o call.wav
python dtmf.py decode call.wav
python hexspeak.py deadbeef cafe babe
python hexspeak.py --leet "bad code"
python leet.py "elite hacker"
```

`dtmf.py` writes real touch tone audio and decodes it back with the Goertzel algorithm. `hexspeak.py` spells words the way 0xDEADBEEF was spelled. `leet.py` is a small leetspeak translator.

## The catalog

<!-- CATALOG:START -->
### Phone phreaking

| Code | What it is | Era | Sources |
|---|---|---|---|
| `2600 Hz` | **The 2600 Hz tone.** A pure tone that AT&T long distance trunks used to signal an idle line. Playing it down a call let phreakers take control of the trunk and then send routing tones of their own. Modern networks keep signaling out of band, so the trick no longer works. | 1960s to 1970s | [1](https://en.wikipedia.org/wiki/Blue_box) |
| `Cap'n Crunch whistle` | **Cap'n Crunch whistle.** A toy whistle packed in Cap'n Crunch cereal boxes made a 2600 Hz tone when one hole was covered. John Draper took the handle Captain Crunch from it. The blind phreaker Joe Engressia had found the tone earlier by whistling it himself. | early 1970s | [1](https://en.wikipedia.org/wiki/John_Draper) [2](https://en.wikipedia.org/wiki/Blue_box) |
| `Blue box` | **The blue box.** An electronic generator for 2600 Hz plus the routing tones. AT&T security seized its first one around 1962, so the idea was already old by the time the press found it. | 1960s to 1980s | [1](https://en.wikipedia.org/wiki/Blue_box) |
| `Esquire, October 1971` | **Secrets of the Little Blue Box.** Ron Rosenbaum's magazine article that took phreaking to the general public. Steve Jobs and Steve Wozniak both read it, and it is often cited as an influence on them. | 1971 | [1](https://en.wikipedia.org/wiki/Blue_box) |
| `697 770 852 941 Hz rows, 1209 1336 1477 1633 Hz columns` | **Touch tone (DTMF) keypad.** Every key on a phone pad is two sine waves played together, one for its row and one for its column. The fourth column holds the A B C D keys that most phones never had. dtmf.py in this repo writes and decodes them. | 1960s onward | [1](https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling) |

### Modems and war dialing

| Code | What it is | Era | Sources |
|---|---|---|---|
| `Demon dialer and war dialer` | **War dialing.** A program that calls a list or range of numbers and logs the ones that answer with modem handshake tones. The Jargon File says war dialers evolved from earlier demon dialers that just kept redialing one number. | 1980s to 1990s | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) [2](https://en.wikipedia.org/wiki/Demon_dialing) |
| `WarGames (1983)` | **WarGames.** The film that put dialing numbers in bulk to find computers into popular culture, and the name war dialing is tied to it. The practice was older and went by demon dialing before the film. | 1983 | [1](https://en.wikipedia.org/wiki/WarGames) [2](https://en.wikipedia.org/wiki/Demon_dialing) |
| `AT` | **The Hayes Smartmodem command set.** Dennis Hayes and Dale Heatherington built it for the 300 baud Hayes Smartmodem in 1981. Every command starts with AT, short for attention, so the modem knows a command is coming. | 1981 | [1](https://en.wikipedia.org/wiki/Hayes_AT_command_set) |
| `ATDT5550199` | **Dial a number.** D is dial and T is tone dialing. ATDP does the same with pulse dialing for old rotary lines. | 1980s to 1990s | [1](https://en.wikipedia.org/wiki/Hayes_AT_command_set) |
| `ATH0` | **Hang up.** Puts the modem back on hook, which ends the call. ATH1 takes the line off hook. | 1980s to 1990s | [1](https://en.wikipedia.org/wiki/Hayes_AT_command_set) |
| `ATZ` | **Reset the modem.** Loads the stored default profile. Wait about two seconds before sending the next command. | 1980s to 1990s | [1](https://en.wikipedia.org/wiki/Hayes_AT_command_set) |

### Unix, Linux and terminal secrets

| Code | What it is | Era | Sources |
|---|---|---|---|
| `Alt + SysRq + R E I S U B` | **Magic SysRq rescue sequence.** The Linux kernel answers the SysRq key even when the desktop is frozen. In order, r takes the keyboard back from the display server, e asks every process to exit, i kills the rest, s syncs disks, u remounts them read only and b reboots. The b reboots instantly, which is why s and u come first. Only use it on a machine that is really hung. | Linux | [1](https://docs.kernel.org/admin-guide/sysrq.html) |
| `apt-get moo` | **Super Cow Powers.** Prints an ASCII cow that asks whether you have mooed today. apt-get help also admits that this APT has Super Cow Powers. | Debian | [1](https://www.digitalocean.com/community/tutorials/top-10-linux-easter-eggs) |
| `aptitude -vvvvv moo` | **The aptitude denial ladder.** Plain aptitude moo denies there are any easter eggs. Each extra v makes it more exasperated, and at five it gives in. | Debian | [1](https://nesbitt.io/2026/04/03/package-manager-easter-eggs) |
| `emerge --moo and zypper moo` | **Cows in other package managers.** Gentoo's emerge draws Larry the Cow. openSUSE's zypper draws a hedgehog by default. | Linux | [1](https://nesbitt.io/2026/04/03/package-manager-easter-eggs) |
| `telnet towel.blinkenlights.nl` | **Star Wars in ASCII over telnet.** Plays Star Wars Episode IV as ASCII frames in your terminal. The server answered on port 23 when this repo was written on 2026-11-24, so it still runs. Windows needs the Telnet Client feature switched on first. | 2000s | [1](https://www.tomsguide.com/how-to/how-to-watch-star-wars-in-ascii-on-windows-10) [2](https://www.physicsforums.com/threads/ascii-starwars-enjoy-the-classic-movie-on-telnet-towel-blinkenlights-nl.116684) |
| `M-x doctor` | **The Emacs therapist.** A chatbot psychotherapist that ships inside Emacs, in the tradition of ELIZA. | 1980s onward | [1](https://www.gnu.org/software/emacs/manual/html_node/emacs/Amusements.html) [2](https://en.wikipedia.org/wiki/ELIZA) |
| `xyzzy` | **The canonical magic word.** From Colossal Cave Adventure. Typed at the right spot in the cave it moves you between two distant places. The Jargon File uses it as the word to shout when something works by magic, and lists plugh as its sibling. | 1970s | [1](https://en.wikipedia.org/wiki/Xyzzy_(computing)) [2](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |

### Hexspeak and magic numbers

| Code | What it is | Era | Sources |
|---|---|---|---|
| `0xDEADBEEF` | **DEADBEEF.** Marks memory that is allocated but not yet initialized, so it jumps out of a dump. Solaris uses it for freed kernel memory. IBM RS/6000, 32 bit PowerPC Mac OS and the Commodore Amiga used it as a debug value. | 1980s onward | [1](https://en.wikipedia.org/wiki/Hexspeak) |
| `0xCAFEBABE` | **CAFEBABE.** The first four bytes of every Java class file, and of Mach-O universal binaries. The popular explanation is a coffee joke, although the 1996 newsgroup answer about it was only a guess. | 1990s | [1](https://en.wikipedia.org/wiki/Hexspeak) [2](https://www.artima.com/insidejvm/whyCAFEBABE.html) |
| `0xFEE1DEAD` | **FEE1DEAD.** A magic number the Linux reboot system call expects, so a stray call cannot restart the machine by accident. Read it aloud as feel dead. | Linux | [1](https://en.wikipedia.org/wiki/Hexspeak) |
| `0x1BADB002` | **1BADB002.** The magic value in the Multiboot header that boot loaders look for in a kernel image. | Linux and GRUB | [1](https://en.wikipedia.org/wiki/Hexspeak) |

### Mobile phone codes

| Code | What it is | Era | Sources |
|---|---|---|---|
| `*#06#` | **Show the IMEI.** Displays the 15 digit IMEI hardware ID on most GSM phones. It is a general GSM code and not specific to Nokia. | 1990s onward | [1](https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity) |
| `*#0000#` | **Nokia software version.** Shows the software version on many Nokia models. Nokia never documented these codes officially, so what works depends on the model and firmware. | 1990s to 2000s | [1](https://news.softpedia.com/news/10-Nokia-Secret-Codes-193581.shtml) |
| `*#92702689#` | **Nokia service info.** A service information screen on some Nokia models. Fan lists disagree on exactly what it shows, so treat it as folklore and expect it to vary by model. | 1990s to 2000s | [1](https://news.softpedia.com/news/10-Nokia-Secret-Codes-193581.shtml) |

### Cheat codes

| Code | What it is | Era | Sources |
|---|---|---|---|
| `Up Up Down Down Left Right Left Right B A` | **The Konami Code.** Kazuhisa Hashimoto added it while porting Gradius to the NES in 1986 to make the game easier to test and play. In Gradius it hands you the full power up set. He meant to remove it before release, and then it shipped and became the most famous cheat ever. | 1986 | [1](https://en.wikipedia.org/wiki/Konami_Code) [2](https://en.wikipedia.org/wiki/Kazuhisa_Hashimoto) [3](https://www.npr.org/2020/02/26/809622331/kazuhisa-hashimoto-creator-of-famous-konami-code-gaming-cheat-dies) |
| `Konami Code on the Contra title screen` | **The 30 lives code.** The same sequence in the 1988 NES version of Contra gave 30 lives. It is the use most people remember, and the reason the code is also called the Contra Code. | 1988 | [1](https://en.wikipedia.org/wiki/Konami_Code) |
| `IDDQD` | **Doom god mode.** Makes the player immune to damage, the classic god mode of the 1990s. | 1993 | [1](https://mirrors.lug.mtu.edu/idgames/docs/rgcd-pips/cheats) |
| `IDKFA` | **Doom all weapons.** Gives maximum ammo, armor and weapons. Its sibling IDFA does the same but leaves out the colored keys. | 1993 | [1](https://mirrors.lug.mtu.edu/idgames/docs/rgcd-pips/cheats) |
| `IDSPISPOPD` | **Doom walk through walls.** Walk through walls in the original Doom, which the cheat lists call zero clipping. Doom II replaced it with the plainer IDCLIP. | 1993 | [1](https://mirrors.lug.mtu.edu/idgames/docs/rgcd-pips/cheats) |

### Windows secrets

| Code | What it is | Era | Sources |
|---|---|---|---|
| `GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}` | **Windows God Mode folder.** Name a new folder like this and Explorer turns it into one long list of roughly 250 settings and Control Panel tasks. Pressing Win+R and running shell:::{ED7BA470-8E54-465E-825C-99712043E01C} opens the same view. GodMode is only a nickname and the label before the dot can be anything. | Windows 7 onward | [1](https://learn.microsoft.com/en-us/archive/blogs/deploymentguys/windows-7-godmode-and-other-folder-shortcuts) |

### Search operators

| Code | What it is | Era | Sources |
|---|---|---|---|
| `intitle: inurl: filetype: site:` | **Google dorks.** Johnny Long started collecting clever Google queries as googleDorks in December 2002, and the Google Hacking Database formally began in 2004. He passed it to Offensive Security in 2010 and it now lives on at Exploit-DB. Today it is mainly a defensive habit, used to check what your own site leaks. | 2002 to 2010 | [1](https://en.wikipedia.org/wiki/Google_hacking) |

### Texts, groups and history

| Code | What it is | Era | Sources |
|---|---|---|---|
| `The Conscience of a Hacker` | **The Hacker Manifesto.** Written by Loyd Blankenship as The Mentor on 8 January 1986 and published in Phrack volume 1 issue 7. It is the best known text of hacker culture, and it is short enough to read in five minutes. | 1986 | [1](http://www.phrack.org/archives/issues/7/3.txt) [2](https://en.wikipedia.org/wiki/Hacker_Manifesto) |
| `Phrack` | **Phrack.** The underground ezine of the mid 1980s that carried the Hacker Manifesto and Phrack's own history of the Legion of Doom. It is still published. | 1985 onward | [1](https://en.wikipedia.org/wiki/Phrack) [2](https://phrack.org/issues/31/5) |
| `2600: The Hacker Quarterly` | **2600 magazine.** Print magazine named after the phreaking tone. Its editor writes as Emmanuel Goldstein, a name borrowed from Orwell's 1984. The real name is Eric Corley. | 1984 onward | [1](https://en.wikipedia.org/wiki/2600:_The_Hacker_Quarterly) |
| `Legion of Doom` | **Legion of Doom.** An early US hacking group. Phrack's own history dates it from 1984 and says the name came from the Super Friends cartoon. | 1984 to 1990 | [1](https://archives.phrack.org/issues/31/5.txt) [2](https://en.wikipedia.org/wiki/Legion_of_Doom_(hacking)) |
| `Masters of Deception` | **Masters of Deception.** A New York group that split off from the Legion of Doom. The so called Great Hacker War between the two is disputed, and Phiber Optik later called it a complete fabrication. | late 1980s | [1](https://en.wikipedia.org/wiki/Masters_of_Deception) [2](https://en.wikipedia.org/wiki/Great_Hacker_War) |
| `Chaos Computer Club` | **Chaos Computer Club.** The German hacker club, usually named next to the Legion of Doom as one of the first hacking groups. | 1980s onward | [1](https://en.wikipedia.org/wiki/Chaos_Computer_Club) |
| `Morris worm, 2 November 1988` | **The Morris worm.** One of the oldest internet worms and the first to get major press. It hit around 6,000 of roughly 60,000 connected machines. A flaw in its self check let it reinfect machines until they crawled. It led to the first felony conviction under the 1986 Computer Fraud and Abuse Act and to the first CERT. | 1988 | [1](https://en.wikipedia.org/wiki/Morris_worm) [2](https://st.llnl.gov/news/look-back/1988-morris-worm-internets-first-cyberattack) |
| `The Jargon File` | **The Jargon File.** A dictionary of hacker slang that began at Stanford in 1975 and grew out of the AI lab and PDP-10 communities. It became the book The Hacker's Dictionary in 1983, then Eric Raymond's New Hacker's Dictionary in 1991. | 1975 onward | [1](https://en.wikipedia.org/wiki/Jargon_File) [2](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `1337 5p34k` | **Leetspeak.** Swapping letters for look alike digits and symbols, a habit of the BBS and IRC crowd. leet.py in this repo converts text at three levels. | 1980s to 2000s | [1](https://en.wikipedia.org/wiki/Leet) |

### Jargon File slang

| Code | What it is | Era | Sources |
|---|---|---|---|
| `foo` | **foo.** The first of the standard metasyntactic variables, followed by bar, baz, qux and quux. Also a sample name for any program or scratch file. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `frob` | **frob.** From the MIT Tech Model Railroad Club, where it meant a protruding arm. By extension any small random object, and as a verb to fiddle with something. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `mung` | **mung.** To change a file in big, irreversible ways, or to destroy it by accident. Early on it was said to stand for Mash Until No Good, later recast as the recursive Mung Until No Good. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `kluge` | **kluge.** A clever but ugly fix that solves a nasty case in a hurry. It leans on the German word klug, meaning clever. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `VAXen and boxen` | **VAXen and boxen.** Fanciful plurals by analogy with ox and oxen. VAXen came first for VAX computers, then boxen for commodity Unix machines that are all interchangeable. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `wedged` | **wedged.** Stuck and unable to make progress without help, which is different from crashed. A wedged system is still trying to do something. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `Heisenbug` | **Heisenbug.** A bug that vanishes or changes behavior when you try to probe it, named after Heisenberg's uncertainty principle. Running a debugger can be enough to hide it. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `bit rot` | **bit rot.** The joke theory that unused programs stop working over time even though nothing changed, as if the bits were radioactive. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `smoke test` | **smoke test.** Power the hardware on and watch for smoke. Later stretched to mean the first run of new software after a big change. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `grok` | **grok.** From Heinlein's novel Stranger in a Strange Land. To understand something completely and in a global sense. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
| `cruft` | **cruft.** Unpleasant buildup, and in code the redundant or superseded leftovers nobody dares delete. The Tech Model Railroad Club dictionary noted that attacking it with a broom only makes more. | Jargon File | [1](https://stuff.mit.edu/afs/sipb.mit.edu/user/marc/stuff.athena/jargon/jarg400.txt) |
<!-- CATALOG:END -->

## How the entries were checked

Every entry links to at least one source. The slang entries were checked against the text of the Jargon File 4.0.0. The Doom entries come from the idgames cheat list. The Nokia codes were never officially documented and depend on the model, so they are marked as folklore. Where sources disagree, the entry says so. The catalog was last checked on 2026-11-24.

## Safety note

This is history, trivia and harmless fun. The 2600 Hz trick has not worked on real phone networks for decades, and dialing a stranger's lines in bulk is illegal in many places. Do not run the SysRq reboot or any phone service code on a machine or phone you care about unless you know what it does.

## Contributing

Add an entry to `codes.json` with at least one working source link, then run:

```bash
python render_readme.py
```

`python render_readme.py --check` fails when the README tables no longer match `codes.json`. Keep entries factual, sourced and harmless.

## License

MIT. See [LICENSE](LICENSE).
