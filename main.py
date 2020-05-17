import json

import keyboard

from pydcs import DCS
from pywebgci import ImportConvert

class Main:
    def __init__(self):
        self.ic = ImportConvert()
        self.game = DCS()
    
    def loop(self, coord='MGRS', name=True):
        clipboard = self.ic.clipimport()
        name, lat, lon, alt = self.ic.formatter(clipboard)
        
        if name: self.game.nametodcs(name)

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
                        lambda: main.loop(coord=keys["coordinateType"],
                                     name=keys["sendWaypointName"]))
    keyboard.wait(keys["keybinds"]["exit"])
