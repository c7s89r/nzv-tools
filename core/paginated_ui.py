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
    ("faker", [
        ("50", "faker tools"),
    ]),
    ("system", [
        ("30", "base64 codec"), ("31", "system info"), ("32", "ip pinger"),
        ("33", "obfuscator"), ("34", "web cloner"), ("35", "qr code gen"),
        ("60", "app info"), ("61", "app config"), ("64", "proxy scraper"),
        ("65", "proxy checker"),
    ]),
    ("web", [
        ("70", "guns.lol views"),
    ]),
]

class PaginatedUI:
    @staticmethod
    def draw_logo(colors):
        tw = shutil.get_terminal_size().columns
        fox = [
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠙⠻⢶⣄⡀⠀⠀⠀⢀⣤⠶⠛⠛⡇⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⣙⣿⣦⣤⣴⣿⣁⠀⠀⣸⠇⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣿⣿⣿⣿⣿⣷⣌⠋⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⡈⢻⣿⡟⢁⣠⣾⣿⣦⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠘⣿⠃⣿⣿⣿⣿⡏⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠛⣰⠿⣆⠛⠁⠀⡀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣦⠀⠘⠛⠋⠀⣴⣿⠁⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣏⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠀⠀⠀⠾⢿⣿⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠟⠋⣁⣠⣤⣤⡶⠶⠶⣤⣄⠈⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⢰⣿⣿⣮⣉⣉⣉⣤⣴⣶⣿⣿⣋⡥⠄⠀⠀⠀⠀⠉⢻⣄⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣁⣤⣀⣀⣤⣤⣤⣤⣄⣿⡄⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        ]
        for l in fox:
            print(Colorate.Horizontal(colors["banner"], l.center(tw)))

        stats = ""
        if psutil:
            try:
                cpu = psutil.cpu_percent()
                ram = psutil.virtual_memory().percent
                stats = f"  cpu: {cpu:.0f}%  ram: {ram:.0f}%"
            except:
                pass
        if stats:
            print(Colorate.Horizontal(colors["txt"], stats.rjust(tw)))
        print()

    @staticmethod
    def draw_all_tools(colors):
        tw = shutil.get_terminal_size().columns
        box_w = min(90, tw - 4)
        margin = " " * max(0, (tw - box_w) // 2)

        for cat_name, tools in CATEGORIES:
            print(margin + Colorate.Horizontal(colors["head"], f"  {cat_name}"))
            col_w = (box_w - 2) // 3
            for i in range(0, len(tools), 3):
                line = ""
                for j in range(3):
                    if i + j < len(tools):
                        k, n = tools[i + j]
                        entry = f"  {k.zfill(2)}  {n}"
                        line += entry + " " * max(1, col_w - len(entry))
                    else:
                        line += " " * col_w
                print(margin + Colorate.Horizontal(colors["txt"], line))
            print()

        print(margin + Colorate.Horizontal(colors["txt"], "  60  app info    61  config    99  exit"))
        print(margin + Colorate.Horizontal(colors["num"], "  " + "─" * (box_w - 2)))

    @classmethod
    def draw_dashboard(cls):
        clr()
        colors = Theme.get_colors()
        cls.draw_logo(colors)
        cls.draw_all_tools(colors)

    @staticmethod
    def draw_card_box(title, items):
        colors = Theme.get_colors()
        tw = shutil.get_terminal_size().columns
        box_w = max(50, min(80, tw - 6))
        margin = " " * max(0, (tw - box_w) // 2)

        print(margin + Colorate.Horizontal(colors["head"], f"  {title}"))
        print(margin + Colorate.Horizontal(colors["num"], "  " + "─" * (box_w - 4)))

        list_items = list(items.items())
        col_w = box_w // 2
        for i in range(0, len(list_items), 2):
            k1, v1 = list_items[i]
            k2, v2 = list_items[i + 1] if i + 1 < len(list_items) else ("", "")
            c1 = f"  {k1}  {v1:<{col_w - 5}}"
            c2 = f"  {k2}  {v2:<{col_w - 5}}" if k2 else ""
            print(margin + Colorate.Horizontal(colors["txt"], c1 + c2))

        print(margin + Colorate.Horizontal(colors["num"], "  " + "─" * (box_w - 4)))
