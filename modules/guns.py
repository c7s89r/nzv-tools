import requests
import threading
import time
import random
import sys

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0",
]

def send_view(url):
    try:
        h = {"User-Agent": random.choice(USER_AGENTS), "Accept-Language": "en-US,en;q=0.9"}
        r = requests.get(url, headers=h, timeout=10)
        return r.status_code == 200
    except:
        return False

def guns_views_bot():
    from core.display import Theme, Colorate, Colors, clr, get_config
    cl = Theme.get_colors()
    clr()
    print(Colorate.Horizontal(cl["head"], "  guns.lol views bot\n"))

    url = input("  target url: ").strip()
    if not url.startswith("http"):
        url = "https://guns.lol/" + url

    try:
        total = int(input("  views to send: ") or 100)
    except:
        total = 100

    try:
        threads = int(input("  threads (5): ") or 5)
    except:
        threads = 5

    sent = 0
    failed = 0
    lock = threading.Lock()

    def worker():
        nonlocal sent, failed
        while sent + failed < total:
            ok = send_view(url)
            with lock:
                if ok:
                    sent += 1
                else:
                    failed += 1
                sys.stdout.write(f"\r  sent: {sent}  failed: {failed}  /  {total}")
                sys.stdout.flush()
            time.sleep(0.1)

    runners = []
    for _ in range(min(threads, total)):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        runners.append(t)

    for t in runners:
        t.join()

    print(f"\n\n  done — {sent} views sent, {failed} failed")
    input("\n  enter to continue")
