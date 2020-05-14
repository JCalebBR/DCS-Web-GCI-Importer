import keyboard
import json

from pydcs import DCS
from pywebgci import ImportConvert


def main(coord='MGRS', name=True):
    ic = ImportConvert()
    clipboard = ic.clipimport()
    lat, lon, alt, utype = ic.formatter(clipboard)
    game = DCS()
    if coord == 'DD':
        lat, lon = ic.dmstodd(lat, lon)
        game.ddtodcs(lat, lon)
    elif coord == 'MGRS':
        fmgrs = ic.dmstomgrs(lat, lon)
        game.mgrstodcs(fmgrs)
    else:
        pass

    game.elevtodcs(alt)

    if name: game.nametodcs(utype)


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        keys = json.loads(f.read())
    keyboard.add_hotkey(keys["keybinds"]["copyToDCS"],
                        lambda: main(coord=keys["coordinateType"],
                                     name=keys["sendWaypointName"]))
    keyboard.wait(keys["keybinds"]["exit"])
