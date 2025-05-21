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

**Track your terminal `clear` habits with style.**

## Features

- Replaces your default `clear` command seamlessly
- Logs every clear invocation locally for detailed tracking
- Supports useful flags:
  - `--stats` — display detailed clear stats with charts
  - `--reset` — reset your clear count and logs
  - `--ascii` — display fun ASCII art
- Easy installation via `pip`
- Encourages productive and fun terminal usage tracking

## Example

```bash
$ clear --stats
[🧼] You've cleared 69 times — just getting started!

🧹 Terminal Clear Stats (Last 10 days)

2025-05-21 | ██████████████████████████████ 3

Average clears per day: 3.0
```

## Installation

```bash
pip install cleartrack
```

Then add the following alias to your shell config `.bashrc`, `.zshrc`, or `.config/fish/config.fish`:

```bash
alias clear="cleartrack"
```

Reload your shell configuration:
```bash
source ~/.bashrc  # or source ~/.zshrc, depending on your shell
```

## Usage
| Command          | Description                        |
| ---------------- | ---------------------------------- |
| `clear`          | Clear screen and increment counter |
| `clear --stats`  | Show detailed clear stats          |
| `clear --reset`  | Reset clear counter and logs       |
| `clear --ascii`  | Display ASCII art                  |

## Developer Mode

```bash
git clone https://github.com/anilrajrimal1/cleartrack.git
cd cleartrack
pip install -e .
```


## 📄 License

MIT © [Anil Raj Rimal](https://github.com/anilrajrimal1)

> Clear the noise. Count the habit. — `cleartrack`