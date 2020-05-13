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
        print(fmgrs)
        game.mgrstodcs(fmgrs)
        game.elevtodcs(alt)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    keyboard.add_hotkey('Shift+C', main)
    keyboard.wait('esc')
