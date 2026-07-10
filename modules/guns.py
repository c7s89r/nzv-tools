import threading
import time
import random
import sys

def guns_views_bot():
    from core.display import Theme, Colorate, Colors, clr, get_config
    cl = Theme.get_colors()
    clr()
    print(Colorate.Horizontal(cl["head"], "  guns.lol views bot\n"))

    username = input("  target: ").strip().replace("https://guns.lol/", "")
    if not username:
        username = "crxsh"

    try:
        total = int(input("  views to send: ") or 10)
    except:
        total = 10

    try:
        threads = int(input("  threads (5): ") or 5)
    except:
        threads = 5

    try:
        import cloudscraper
    except ImportError:
        print(Colorate.Horizontal(cl["txt"], "  installing cloudscraper..."))
        import subprocess, sys as _sys
        subprocess.check_call([_sys.executable, "-m", "pip", "install", "cloudscraper", "-q"])
        import cloudscraper

    scraper = cloudscraper.create_scraper(delay=5)
    hdrs = {
        "accept": "*/*",
        "origin": "https://guns.lol",
        "referer": f"https://guns.lol/{username}",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36",
        "username": username,
    }

    sent = 0
    failed = 0
    lock = threading.Lock()

    def worker():
        nonlocal sent, failed
        while sent + failed < total:
            try:
                r = scraper.post(f"https://guns.lol/api/view/{username}", headers=hdrs, timeout=15)
                ok = r.status_code == 200
            except:
                ok = False
            with lock:
                if ok:
                    sent += 1
                else:
                    failed += 1
                sys.stdout.write(f"\r  sent: {sent}  failed: {failed}  /  {total}  ")
                sys.stdout.flush()

    runners = []
    for _ in range(min(threads, total)):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        runners.append(t)

    for t in runners:
        t.join()

    print(f"\n\n  done — {sent} sent, {failed} failed")
    input("\n  enter to continue")
