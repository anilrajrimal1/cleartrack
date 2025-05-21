#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path
from datetime import datetime

COUNT_FILE = Path.home() / ".cleartrack"
LOG_FILE = Path.home() / ".cleartrack.log"

def get_count():
    if COUNT_FILE.exists():
        with open(COUNT_FILE, "r") as f:
            return int(f.read().strip() or 0)
    return 0

def save_count(count):
    with open(COUNT_FILE, "w") as f:
        f.write(str(count))

def log_usage():
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()}\n")

def print_count(count, stats_mode=False):
    if stats_mode:
        print(f"\033[92m[🧹] You have cleared your terminal {count} times. Keep it clean!\033[0m")
    else:
        print(f"\033[92m[🧹] Cleared {count} times.\033[0m")

def print_ascii():
    print(r"""
_________ .__                        __                        __    
\_   ___ \|  |   ____ _____ ________/  |_____________    ____ |  | __
/    \  \/|  | _/ __ \\__  \\_  __ \   __\_  __ \__  \ _/ ___\|  |/ /
\     \___|  |_\  ___/ / __ \|  | \/|  |  |  | \// __ \\  \___|    < 
 \______  /____/\___  >____  /__|   |__|  |__|  (____  /\___  >__|_ \
        \/          \/     \/                        \/     \/     \/
    """)

def main():
    args = sys.argv[1:]

    if "--stats" in args:
        print_count(get_count(), stats_mode=True)
        return

    if "--reset" in args:
        save_count(0)
        print("Counter reset to 0.")
        return

    if "--ascii" in args:
        print_ascii()
        return

    count = get_count() + 1
    save_count(count)
    log_usage()

    subprocess.run(["clear"])
    print_count(count, stats_mode=False)

if __name__ == "__main__":
    main()