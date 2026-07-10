import os
import shutil
from core.display import Theme, Colorate, Colors, clr, get_config

PAGES = [
    {
        "title": "discord",
        "tools": [
            ("1", "webhook tools"),
            ("2", "token tools"),
            ("3", "nitro generator"),
            ("4", "server info"),
            ("5", "bot invite gen"),
            ("6", "selfbot"),
            ("7", "server cloner"),
            ("8", "nuke bot"),
            ("9", "username checker"),
        ]
    },
    {
        "title": "osint",
        "tools": [
            ("10", "port scanner"),
            ("11", "whois lookup"),
            ("12", "dns lookup"),
            ("13", "metadata scan"),
            ("14", "dox tracker"),
            ("15", "dox creator"),
            ("16", "phone lookup"),
            ("17", "email lookup"),
        ]
    },
    {
        "title": "malicious",
        "tools": [
            ("20", "email bomber"),
            ("21", "crypto clipper"),
            ("22", "vuln scanner"),
            ("23", "ddos attack"),
            ("24", "stealer builder"),
            ("25", "keylogger builder"),
            ("26", "ip grabber"),
            ("27", "rat builder"),
            ("28", "wallet bruteforce"),
        ]
    },
    {
        "title": "roblox",
        "tools": [
            ("40", "user info"),
            ("41", "cookie info"),
            ("42", "cookie login"),
            ("43", "group info"),
            ("44", "asset dl"),
            ("45", "name history"),
            ("46", "username checker"),
            ("47", "cookie refresher"),
        ]
    },
    {
        "title": "faker",
        "tools": [
            ("50", "faker tools"),
            ("34", "web cloner"),
            ("35", "qr code gen"),
        ]
    },
    {
        "title": "system",
        "tools": [
            ("30", "base64 codec"),
            ("31", "system info"),
            ("32", "ip pinger"),
            ("33", "obfuscator"),
            ("60", "app info"),
            ("61", "app config"),
            ("64", "proxy scraper"),
            ("65", "proxy checker"),
        ]
    },
    {
        "title": "web",
        "tools": [
            ("70", "guns.lol views"),
            ("99", "exit"),
        ]
    },
]


class PaginatedUI:
    @staticmethod
    def get_layout_width():
        return min(80, shutil.get_terminal_size().columns - 4)

    @staticmethod
    def get_margin(box_w):
        return " " * max(0, (shutil.get_terminal_size().columns - box_w) // 2)

    @staticmethod
    def draw_logo(colors):
        tw = shutil.get_terminal_size().columns
        print(Colorate.Horizontal(colors["banner"], "nzv tools".center(tw)))
        print()

    @staticmethod
    def draw_menu(active_idx, colors, box_w, margin):
        page = PAGES[active_idx]
        inner = box_w - 2

        print(margin + Colorate.Horizontal(colors["head"], f"  {page['title']}"))
        print(margin + Colorate.Horizontal(colors["num"], "  " + "─" * (inner - 2)))

        tools = page["tools"]
        for i in range(0, len(tools), 2):
            left = tools[i]
            right = tools[i + 1] if i + 1 < len(tools) else None
            lk = str(left[0]).zfill(2)
            ln = left[1]
            line = f"  {lk}  {ln}"
            pad = (inner // 2) - len(f"  {lk}  {ln}")
            if pad > 0:
                line += " " * pad
            if right:
                rk = str(right[0]).zfill(2)
                rn = right[1]
                line += f"  {rk}  {rn}"
            print(margin + Colorate.Horizontal(colors["txt"], line))

        print(margin + Colorate.Horizontal(colors["num"], "  " + "─" * (inner - 2)))

    @staticmethod
    def draw_footer(colors, box_w, margin):
        print(margin + Colorate.Horizontal(colors["txt"], f"  n next  p prev  60 info  61 config  99 exit"))

    @classmethod
    def draw_dashboard(cls, active_idx):
        clr()
        colors = Theme.get_colors()
        box_w = cls.get_layout_width()
        margin = cls.get_margin(box_w)
        cls.draw_logo(colors)
        cls.draw_menu(active_idx, colors, box_w, margin)
        print()
        cls.draw_footer(colors, box_w, margin)

    @staticmethod
    def draw_card_box(title, items):
        colors = Theme.get_colors()
        tw = shutil.get_terminal_size().columns
        box_w = max(50, min(80, tw - 6))
        inner = box_w - 2
        margin = " " * max(0, (tw - box_w) // 2)

        print(margin + Colorate.Horizontal(colors["head"], f"  {title}"))
        print(margin + Colorate.Horizontal(colors["num"], "  " + "─" * (inner - 2)))

        list_items = list(items.items())
        col_w = inner // 2
        for i in range(0, len(list_items), 2):
            k1, v1 = list_items[i]
            k2, v2 = list_items[i + 1] if i + 1 < len(list_items) else ("", "")
            c1 = f"  {k1}  {v1:<{col_w - 5}}"
            c2 = f"  {k2}  {v2:<{col_w - 5}}" if k2 else ""
            print(margin + Colorate.Horizontal(colors["txt"], c1 + c2))

        print(margin + Colorate.Horizontal(colors["num"], "  " + "─" * (inner - 2)))
