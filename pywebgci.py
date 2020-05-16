import mgrs
import pyautogui
import pyperclip

from pylog import Logger
from pydcs import DCS


class ImportConvert:
    def __init__(self):
        self.log = Logger()

    def clipimport(self):
        clipboard = None
        pyautogui.hotkey('Ctrl', 'Insert')
        clipboard = pyperclip.paste()
        self.log.debug(clipboard)

        clipboard = clipboard.splitlines()

        self.log.debug(clipboard)

        return clipboard

    def formatter(self, clipboard):
        def formatlat(latitude):
            latitude = latitude.replace('°', '').replace('\'', '').replace(
                '\"', '').replace('Latitude:', '').replace(' ', '')

            self.log.debug(latitude)

            return latitude

        def formatlon(longitude):
            longitude = longitude.replace('°', '').replace('\'', '').replace(
                '\"', '').replace('Longitude:', '').replace(' ', '')

            self.log.debug(longitude)

            return longitude

        def formatalt(altitude):
            real_altitude = list()

            altitude = altitude.replace('Altitude:', '').replace(' ', '')

            for char in altitude:
                real_altitude.append(char)
                if char == 'T':
                    break
            real_altitude = ''.join(real_altitude)
            real_altitude = real_altitude.replace('FT', '')
            altitude = real_altitude

            self.log.debug(altitude)

            return altitude

        # def formatutype(utype):
        #     utype = utype.replace('Unit Type:', '')
        #     self.log.debug(utype)
        #     return utype

        def formatname(name):
            name = name.replace('-', ' ')

            self.log.debug(name)

            return name

        for idx, line in enumerate(clipboard):
            if idx == 0:
                name = formatname(name)
            else:
                if not line.find('Latitude:'):
                    latitude = formatlat(line)
                if not line.find('Longitude:'):
                    longitude = formatlon(line)
                if not line.find('Altitude:'):
                    altitude = formatalt(line)

        return latitude, longitude, altitude, name

    def dmstomgrs(self, latitude, longitude):
        utm = mgrs.MGRS()
        latitude = utm.dmstodd(latitude)
        longitude = utm.dmstodd(longitude)
        fmgrs = utm.toMGRS(latitude, longitude, MGRSPrecision=5)
        fmgrs = fmgrs.decode('utf-8')

        self.log.debug(fmgrs)

        return fmgrs

    def dmstodd(self, latitude, longitude):
        utm = mgrs.MGRS()
        latitude = utm.dmstodd(latitude)
        longitude = utm.dmstodd(longitude)

        self.log.debug(latitude)
        self.log.debug(longitude)

        return latitude, longitude
