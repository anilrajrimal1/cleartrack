                    
        _________ .__                        __                        __    
        \_   ___ \|  |   ____ _____ ________/  |_____________    ____ |  | __
        /    \  \/|  | _/ __ \\__  \\_  __ \   __\_  __ \__  \ _/ ___\|  |/ /
        \     \___|  |_\  ___/ / __ \|  | \/|  |  |  | \// __ \\  \___|    < 
         \______  /____/\___  >____  /__|   |__|  |__|  (____  /\___  >__|_ \
                \/          \/     \/                        \/     \/     \/
                    
# cleartrack CLI

Track your terminal `clear` habits with style.

## Features
- Replaces your `clear` command
- Logs every use
- `--stats`, `--reset`, and `--ascii` modes
- Easily installed via `pip`

## Example
```bash
$ clear
[🧹] Cleared 69 times.

$ clear --stats
[🧹] You have cleared your terminal 69 times. Keep it clean!
```

## Installation
```bash
pip install cleartrack
```
Add this to your `.bashrc` / `.zshrc`:
```bash
alias clear="cleartrack"
```

## Usage
```bash
clear           # clears screen and shows counter
clear --stats   # show counter without clearing
clear --reset   # reset the counter to 0
clear --ascii   # show some fun ascii art
```

## 👺 Developer Mode
```bash
git clone https://github.com/anilrajrimal1/cleartrack.git
cd cleartrack
pip install -e .
```

## 🔖 License
MIT

---

Clear the noise. Count the habit. `cleartrack`.
