import keyboard

from pydcs import DCS
from pywebgci import ImportConvert


def main():
    try:
        ic = ImportConvert()
        game = DCS()
        clipboard = ic.clipimport()
        lat, lon, alt = ic.formatter(clipboard)
        fmgrs = ic.dmstomgrs(lat, lon)
        game.mgrstodcs(fmgrs)
        game.elevtodcs(alt)
    except Exception:
        pass

if __name__ == "__main__":
    keyboard.add_hotkey('Shift+C', main)
    keyboard.wait('esc')