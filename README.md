<pre>
 _________ .__                        __                        __    
 \_   ___ \|  |   ____ _____ ________/  |_____________    ____ |  | __
 /    \  \/|  | _/ __ \\__  \\_  __ \   __\_  __ \__  \ _/ ___\|  |/ /
 \     \___|  |_\  ___/ / __ \|  | \/|  |  |  | \// __ \\  \___|    < 
  \______  /____/\___  >____  /__|   |__|  |__|  (____  /\___  >__|_ \
         \/          \/     \/                        \/     \/     \/ 
</pre>

# cleartrack CLI

[![PyPI version](https://img.shields.io/pypi/v/cleartrack.svg)](https://pypi.org/project/cleartrack)
[![Downloads](https://img.shields.io/pypi/dm/cleartrack.svg)](https://pypi.org/project/cleartrack)
[![Release](https://img.shields.io/github/v/release/anilrajrimal1/cleartrack)](https://github.com/anilrajrimal1/cleartrack/releases)
[![License](https://img.shields.io/github/license/anilrajrimal1/cleartrack)](LICENSE)

Track your terminal `clear` habits with style.

## Features

- Replaces your `clear` command
- Logs every use locally
- `--silent`, `--stats`, `--reset`, and `--ascii` flags
- Easily installable via `pip`
- Fun + productive tracking your random clear hitting habit

## 📸 Example

```bash
$ clear
[🧹] Cleared 69 times.

$ clear --stats
[🧹] You have cleared your terminal 69 times. Keep it clean!
```

---

## Installation

```bash
pip install cleartrack
```

Then add this to your `.bashrc`, `.zshrc`, or `.config/fish/config.fish`:

```bash
alias clear="cleartrack"
```

Reload your shell config:
```bash
source ~/.zshrc  # or ~/.bashrc
```

---

## Usage

```bash
clear            # Clears screen + increments counter
clear --silent   # no output, just logs for tracking
clear --stats    # Show counter without clearing
clear --reset    # Reset the counter to 0
clear --ascii    # Show some fun ASCII art
```

---

## Developer Mode

```bash
git clone https://github.com/anilrajrimal1/cleartrack.git
cd cleartrack
pip install -e .
```

---

## 📄 License

MIT © [Anil Raj Rimal](https://github.com/anilrajrimal1)

---

> Clear the noise. Count the habit. — `cleartrack`