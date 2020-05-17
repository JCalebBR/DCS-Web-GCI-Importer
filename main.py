import json

import keyboard

from pydcs import DCS
from pywebgci import ImportConvert


class Main:
    def __init__(self):
        self.ic = ImportConvert()
        self.game = DCS()

    def copy(self):
        self.clipboard = self.ic.clipimport()

    def paste(self, coord='MGRS', name=True):
        name, lat, lon, alt = self.ic.formatter(self.clipboard)

        if name:
            self.game.nametodcs(name)

        if coord == 'MGRS':
            fmgrs = self.ic.dmstomgrs(lat, lon)
            self.game.mgrstodcs(fmgrs)
        elif coord == 'DD':
            lat, lon = self.ic.dmstodd(lat, lon)
            self.game.ddtodcs(lat, lon)
        else:
            pass

        self.game.elevtodcs(alt)


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        keys = json.loads(f.read())
    main = Main()
    keyboard.add_hotkey(keys["keybinds"]["copyToDCS"],
                        lambda: main.copy())
    keyboard.add_hotkey(keys["keybinds"]["pasteToDCS"],
                        lambda: main.paste(coord=keys["coordinateType"],
                                           name=keys["sendWaypointName"]))
    keyboard.wait(keys["keybinds"]["exit"])
