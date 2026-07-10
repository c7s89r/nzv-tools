import os
import shutil
import time
try:
    import psutil
except ImportError:
    psutil = None

from core.display import Theme, Colorate, clr

CATEGORIES = [
    ("discord", [
        ("1", "webhook tools"), ("2", "token tools"), ("3", "nitro generator"),
        ("4", "server info"), ("5", "bot invite gen"), ("6", "selfbot"),
        ("7", "server cloner"), ("8", "nuke bot"), ("9", "username checker"),
    ]),
    ("osint", [
        ("10", "port scanner"), ("11", "whois lookup"), ("12", "dns lookup"),
        ("13", "metadata scan"), ("14", "dox tracker"), ("15", "dox creator"),
        ("16", "phone lookup"), ("17", "email lookup"),
    ]),
    ("malicious", [
        ("20", "email bomber"), ("21", "crypto clipper"), ("22", "vuln scanner"),
        ("23", "ddos attack"), ("24", "stealer builder"), ("25", "keylogger builder"),
        ("26", "ip grabber"), ("27", "rat builder"), ("28", "wallet bruteforce"),
    ]),
    ("roblox", [
        ("40", "user info"), ("41", "cookie info"), ("42", "cookie login"),
        ("43", "group info"), ("44", "asset dl"), ("45", "name history"),
        ("46", "username checker"), ("47", "cookie refresher"),
    ]),
    ("system", [
        ("30", "base64 codec"), ("31", "system info"), ("32", "ip pinger"),
        ("33", "obfuscator"), ("34", "web cloner"), ("35", "qr code gen"),
        ("60", "app info"), ("61", "app config"), ("64", "proxy scraper"),
        ("65", "proxy checker"),
    ]),
    ("faker", [
        ("50", "faker tools"),
    ]),
    ("web", [
        ("70", "guns.lol views"),
    ]),
]

PAGES = CATEGORIES

class PaginatedUI:
    @staticmethod
    def draw_logo(colors):
        tw = shutil.get_terminal_size().columns
        print(Colorate.Horizontal(colors["head"], "   n z v   t o o l s".center(tw)))
        print()

    @staticmethod
    def draw_tab_bar(colors, page):
        tw = shutil.get_terminal_size().columns
        names = [n for n, _ in CATEGORIES]
        cols = {}
        for i, n in enumerate(names):
            if i == page:
                cols[n] = "banner"
            else:
                cols[n] = "txt"
        parts = []
        for i, n in enumerate(names):
            start = "[" if i == page else " "
            end = "]" if i == page else " "
            c = cols[n]
            parts.append(Colorate.Horizontal(colors[c], f"{start}{n}{end}"))
        bar = "  ".join(parts)
        print(Colorate.Horizontal(colors["num"], " " + "─" * (tw - 2)))
        print(bar.center(tw))
        print(Colorate.Horizontal(colors["num"], " " + "─" * (tw - 2)))
        print()

    @staticmethod
    def draw_page(colors, page_idx):
        tw = shutil.get_terminal_size().columns
        name, tools = PAGES[page_idx]
        col_w = tw // 3
        for i in range(0, len(tools), 3):
            line = ""
            for j in range(3):
                if i + j < len(tools):
                    k, n = tools[i + j]
                    entry = f"  {k.zfill(2)}  {n}"
                    line += entry + " " * max(1, col_w - len(entry))
                else:
                    line += " " * col_w
            print(Colorate.Horizontal(colors["txt"], line))
        print()

    @classmethod
    def draw_dashboard(cls, page=0):
        clr()
        colors = Theme.get_colors()
        cls.draw_logo(colors)
        stats = ""
        if psutil:
            try:
                cpu = psutil.cpu_percent()
                ram = psutil.virtual_memory().percent
                stats = f"cpu: {cpu:.0f}%  ram: {ram:.0f}%"
            except:
                pass
        if stats:
            tw = shutil.get_terminal_size().columns
            print(Colorate.Horizontal(colors["txt"], stats.center(tw)))
        print()
        cls.draw_tab_bar(colors, page)
        cls.draw_page(colors, page)
        tw = shutil.get_terminal_size().columns
        nav = "a/p prev | d/n next | 99 exit"
        print(Colorate.Horizontal(colors["txt"], nav.center(tw)))
        print()

    @staticmethod
    def draw_card_box(title, items):
        colors = Theme.get_colors()
        tw = shutil.get_terminal_size().columns
        box_w = max(50, min(80, tw - 6))
        margin = " " * max(0, (tw - box_w) // 2)
        border = Colorate.Horizontal(colors["num"], "  " + "─" * (box_w - 4))

        print(margin + Colorate.Horizontal(colors["head"], f"  {title}"))
        print(margin + border)

        list_items = list(items.items())
        col_w = box_w // 2
        for i in range(0, len(list_items), 2):
            k1, v1 = list_items[i]
            k2, v2 = list_items[i + 1] if i + 1 < len(list_items) else ("", "")
            c1 = f"  {k1}  {v1:<{col_w - 5}}"
            c2 = f"  {k2}  {v2:<{col_w - 5}}" if k2 else ""
            print(margin + Colorate.Horizontal(colors["txt"], c1 + c2))

        print(margin + border)
