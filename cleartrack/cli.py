#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

COUNT_FILE = Path.home() / ".cleartrack"
LOG_FILE = Path.home() / ".cleartrack.log"
DAILY_FILE = Path.home() / ".cleartrack.daily"

def get_count():
    if COUNT_FILE.exists():
        with open(COUNT_FILE, "r") as f:
            return int(f.read().strip() or 0)
    return 0

def save_count(count):
    with open(COUNT_FILE, "w") as f:
        f.write(str(count))

def log_usage():
    now = datetime.now()
    today = now.date().isoformat()

    with open(LOG_FILE, "a") as f:
        f.write(f"{now.isoformat()}\n")

    daily = defaultdict(int)
    if DAILY_FILE.exists():
        with open(DAILY_FILE) as f:
            for line in f:
                if line.strip():
                    date_str, val = line.strip().split(",")
                    daily[date_str] = int(val)

    daily[today] += 1

    with open(DAILY_FILE, "w") as f:
        for date, val in sorted(daily.items()):
            f.write(f"{date},{val}\n")

def print_count(count, stats_mode=False):
    if stats_mode:
        # Dynamic header message
        if count == 0:
            header = "\033[96m[🧼] You haven't cleared your terminal yet. Try it now!\033[0m"
        elif count < 10:
            header = f"\033[96m[🧼] You've cleared {count} times — just getting started!\033[0m"
        elif count < 100:
            header = f"\033[92m[🧹] You have cleared your terminal {count} times. Keep it clean!\033[0m"
        elif count < 500:
            header = f"\033[93m[🚀] {count} clears — you're on a roll!\033[0m"
        else:
            header = f"\033[91m[💥] {count} clears?! That's next-level terminal hygiene.\033[0m"

        print(header)
        print_daily_bar_chart()
        return

    # Normal clear count messages only every 20 clears
    if count % 20 == 0:
        if count >= 1000:
            print(f"\033[91m[🧨] {count} clears... Terminal hygiene legend?!\033[0m")
        elif count >= 500:
            print(f"\033[91m[💥] {count} clears?! Are you okay? Your terminal's spotless!\033[0m")
        elif count >= 100:
            print(f"\033[91m[🥵] {count} clears — take a break, maybe?\033[0m")
        elif count >= 60:
            print(f"\033[93m[⚠️] {count} clears. That's a lot of cleaning!\033[0m")
        else:
            print(f"\033[96m[🧹] {count} clears and counting. Fresh mind!\033[0m")

def print_daily_bar_chart():
    print("\n\033[1m🧹 Terminal Clear Stats (Last 10 days)\033[0m\n")

    if not DAILY_FILE.exists():
        print("No daily data available yet.\n")
        return

    data = []
    with open(DAILY_FILE) as f:
        for line in f:
            if line.strip():
                date_str, val = line.strip().split(",")
                data.append((date_str, int(val)))

    if not data:
        print("No daily data available yet.\n")
        return

    # Show only last 10 days
    data = data[-10:]
    max_val = max(val for _, val in data)
    max_bar_len = 30

    # Print bar chart
    for date, val in data:
        bar_len = int((val / max_val) * max_bar_len) if max_val else 0
        bar = "█" * bar_len
        print(f"{date} | {bar:<30} {val}")

    # Print average clears per day
    total_clears = sum(val for _, val in data)
    avg = total_clears / len(data)
    print(f"\nAverage clears per day: {avg:.1f}\n")

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
        if DAILY_FILE.exists():
            DAILY_FILE.unlink()
        print("Counter and daily stats reset.")
        return

    if "--ascii" in args:
        print_ascii()
        return

    count = get_count() + 1
    save_count(count)
    log_usage()

    subprocess.run(["clear"])
    print_count(count)

if __name__ == "__main__":
    main()
