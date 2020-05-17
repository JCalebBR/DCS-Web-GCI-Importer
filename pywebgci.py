import mgrs
import pyautogui
import pyperclip
import win32clipboard
from pylog import Logger
import time

class ImportConvert:
    def __init__(self):
        self.log = Logger()

    def clipimport(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
        pyautogui.hotkey('Ctrl', 'Insert')
        time.sleep(1)
        win32clipboard.OpenClipboard()
        clipboard = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        self.log.debug(clipboard)

        clipboard = clipboard.splitlines()

        self.log.debug(clipboard)

        return clipboard

    def formatter(self, clipboard):
        def format_lat(latitude):
            latitude = latitude.replace('°', '').replace('\'', '').replace(
                '\"', '').replace('Latitude:', '').replace(' ', '')

            self.log.debug(latitude)

            return latitude

        def format_lon(longitude):
            longitude = longitude.replace('°', '').replace('\'', '').replace(
                '\"', '').replace('Longitude:', '').replace(' ', '')

            self.log.debug(longitude)

            return longitude

        def format_alt(altitude):
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

        # def format_utype(utype):
        #     utype = utype.replace('Unit Type:', '')
        #     self.log.debug(utype)
        #     return utype

        def format_name(name):
            name = name.replace('-', ' ')

            self.log.debug(name)

            return name

        name = latitude = longitude = altitude = None

        for idx, line in enumerate(clipboard):
            if idx == 0:
                name = format_name(line)
            else:
                if not line.find('Latitude:'):
                    latitude = format_lat(line)
                if not line.find('Longitude:'):
                    longitude = format_lon(line)
                if not line.find('Altitude:'):
                    altitude = format_alt(line)

        return name, latitude, longitude, altitude

    def dmstomgrs(self, latitude, longitude):
        try:
            utm = mgrs.MGRS()
            latitude = utm.dmstodd(latitude)
            longitude = utm.dmstodd(longitude)
            fmgrs = utm.toMGRS(latitude, longitude, MGRSPrecision=5)
            fmgrs = fmgrs.decode('utf-8')

            self.log.debug(fmgrs)

            return fmgrs
        except TypeError as ex:
            self.log.exception(ex)

    def dmstodd(self, latitude, longitude):
        utm = mgrs.MGRS()
        latitude = utm.dmstodd(latitude)
        longitude = utm.dmstodd(longitude)

        self.log.debug(latitude)
        self.log.debug(longitude)

        return latitude, longitude
