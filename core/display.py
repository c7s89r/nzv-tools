# NZV Tools - Terminal Multitool

import os
import sys
import time
import json
import random
import shutil
from core.themes import THEMES
from core.modern_ui import ModernUI

user = os.environ.get('USERNAME', 'Unknown') if os.name == 'nt' else os.environ.get('USER', 'Unknown')
def get_config():
    try:
        if os.path.exists("core/config.json"):
            with open("core/config.json", "r") as f:
                return json.load(f)
    except:
        pass
    return {}

try:
    import pystyle
    from pystyle import Center, System
except ImportError:
    print("Please install pystyle: pip install pystyle")
    sys.exit(1)

class Colors(pystyle.Colors):
    pass

class Colorate:
    @staticmethod
    def Horizontal(color, text, *args, **kwargs):
        cfg = get_config()
        if cfg.get("theme", "blue").lower() == "rainbow":
            return pystyle.Colorate.Horizontal(pystyle.Colors.rainbow, text, *args, **kwargs)
        if isinstance(color, str):
            return f"{color}{text}{pystyle.Colors.reset}"
        return pystyle.Colorate.Horizontal(color, text, *args, **kwargs)

    @staticmethod
    def Vertical(color, text, *args, **kwargs):
        cfg = get_config()
        if cfg.get("theme", "blue").lower() == "rainbow":
            return pystyle.Colorate.Vertical(pystyle.Colors.rainbow, text, *args, **kwargs)
        return pystyle.Colorate.Vertical(color, text, *args, **kwargs)

class Theme:
    @staticmethod
    def get_colors():
        c = get_config().get("theme", "blue").lower()
        t = THEMES.get(c, THEMES["blue"])
        return {
            "banner": t["banner"],
            "head": t["head"],
            "num": t["num"],
            "txt": t["txt"],
            "sub": t["sub"],
            "inp": t["inp"]
        }

    @staticmethod
    def get_matrix_color():
        c = get_config().get("theme", "blue").lower()
        if c == "rainbow": return -1
        m = {"red":196,"purple":93,"green":46,"yellow":226,"pink":201,"cyan":51,"gray":245,"blue":27, "modern_red":196, "modern_purple":93}
        return m.get(c, 27)

def clr():
    System.Clear()

def init_os():
    cfg = get_config()
    ver = cfg.get("version", "1.0.0")
    user = os.environ.get('USERNAME', 'Unknown') if os.name == 'nt' else os.environ.get('USER', 'Unknown')
    try:
        if os.name == 'nt':
            os.system('mode con cols=120 lines=38')
            sys.stdout.write('\x1b[8;38;120t')
            sys.stdout.flush()
        else:
            sys.stdout.write('\x1b[8;38;120t')
            sys.stdout.flush()
    except:
        print("error")
        pass
    System.Title(f"*NZV Tools @ {user} ~ v{ver}")
    cols, rows = shutil.get_terminal_size()
    if cols < 80:
        cl = Theme.get_colors()
        print(Colorate.Horizontal(cl.get("num", ""), f"\n  [!] WARNING: Terminal width is {cols} (less than 80)."))
        print(Colorate.Horizontal(cl.get("txt", ""), "      For the best experience and alignment, please widen your terminal window!\n"))
        time.sleep(3.0)

def type_print(text, delay=0.03):
    cl = Theme.get_colors()
    sys.stdout.write(Colorate.Horizontal(cl["num"], "  [*] "))
    [ (sys.stdout.write(Colorate.Horizontal(cl["txt"], c)), sys.stdout.flush(), time.sleep(delay)) for c in text ]
    sys.stdout.write("\n")

def boot_anim():
    banner = r"""
    ╔══════════════════════════════════════════════╗
    ║                                                  ║
    ║     ███╗   ██╗███████╗██╗   ██╗                ║
    ║     ████╗  ██║╚══███╔╝██║   ██║                ║
    ║     ██╔██╗ ██║  ███╔╝ ██║   ██║                ║
    ║     ██║╚██╗██║ ███╔╝  ╚██╗ ██╔╝                ║
    ║     ██║ ╚████║███████╗ ╚████╔╝                 ║
    ║     ╚═╝  ╚═══╝╚══════╝  ╚═══╝                  ║
    ║                                                  ║
    ║              T E R M I N A L                     ║
    ║              M U L T I T O O L                   ║
    ║                                                  ║
    ╚══════════════════════════════════════════════╝
    """
    cols = Theme.get_colors()
    clr()
    tw = shutil.get_terminal_size().columns
    for line in banner.split('\n'):
        if line.strip():
            print(Colorate.Horizontal(cols["banner"], line.center(tw)))
        else:
            print()
        time.sleep(0.03)
    
    print("\n")
    user = os.environ.get('USERNAME', 'Unknown') if os.name == 'nt' else os.environ.get('USER', 'Unknown')
    seq = [
        f"Initializing NZV kernel [ node: {user} ]...",
        "Loading core modules...",
        "Establishing encrypted channels...",
        "System ready."
    ]
    for s in seq:
        type_print(s, 0.02)
        time.sleep(0.15)
    time.sleep(0.3)

def matrix_effect(cycles=1, color_id=27):
    s = shutil.get_terminal_size()
    cols, rows = s.columns, s.lines
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$+-*/=%\"'#&_(),.;:?!\\|{}<>[]^~"
    d = [0 for _ in range(cols)]
    sys.stdout.write("\033[?25l")
    done, stps = 0, 0
    while done < cycles:
        out = "\033[H"
        for r in range(rows):
            l = ""
            for c in range(cols):
                if d[c] == r: l += "\033[38;5;15m" + random.choice(chars)
                elif d[c] > r and d[c] - 10 < r:
                    cid = random.choice([27, 196, 93, 46, 226, 201, 51]) if color_id == -1 else color_id
                    l += f"\033[38;5;{cid}m" + random.choice(chars)
                else: l += " "
            out += l + "\n"
        for i in range(cols):
            if d[i] > rows:
                d[i] = 0
                if i == 0: done += 1
            elif d[i] == 0:
                if random.random() > 0.95: d[i] = 1
            else: d[i] += 1
        sys.stdout.write(out)
        sys.stdout.flush()
        time.sleep(0.03)
        stps += 1
        if stps > (rows * cycles * 2) + 100: break
    sys.stdout.write("\033[?25h\033[0m\033[2J\033[H")

def print_banner():
    cfg = get_config()
    if cfg.get("theme", "blue").lower().startswith("modern"):
        return ModernUI.print_banner(Colorate, Theme, clr)
    clr()
    cols = Theme.get_colors()
    tw = shutil.get_terminal_size().columns
    banner = r"""
    ███╗   ██╗███████╗██╗   ██╗
    ████╗  ██║╚══███╔╝██║   ██║
    ██╔██╗ ██║  ███╔╝ ██║   ██║
    ██║╚██╗██║ ███╔╝  ╚██╗ ██╔╝
    ██║ ╚████║███████╗ ╚████╔╝ 
    ╚═╝  ╚═══╝╚══════╝  ╚═══╝  
    """
    print(Colorate.Horizontal(cols["banner"], banner.center(tw)))
    print(Colorate.Horizontal(cols["sub"], "─" * 50))
    print()

def menu_opts(options):
    cl = Theme.get_colors()
    _items = list(options.items())
    for i in range(0, len(_items), 2):
        k1, v1 = _items[i]
        _line = Colorate.Horizontal(cl["num"], f"  [{k1}] ") + Colorate.Horizontal(cl["txt"], f"{v1:<25}")
        if i + 1 < len(_items):
            k2, v2 = _items[i+1]
            _line += Colorate.Horizontal(cl["num"], f"  [{k2}] ") + Colorate.Horizontal(cl["txt"], v2)
        print(_line)
    print()

def get_inpt(prompt=None):
    if prompt is None:
        prompt = f"{user}@nzv:~#"
    else:
        prompt = prompt.replace("nzv@root/", f"{user}@nzv/")
        prompt = prompt.replace("nzv@", f"{user}@nzv/")
        
    cl = Theme.get_colors()
    _prmpt = f"\n  {prompt} "
    return input(Colorate.Horizontal(cl["inp"], _prmpt))
