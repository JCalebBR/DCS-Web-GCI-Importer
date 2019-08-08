import mgrs
import pyautogui
import pyperclip

from pydcs import DCS


class ImportConvert:
    def clipimport(self):
        pyautogui.hotkey('Ctrl','Insert')
        clipboard = pyperclip.paste()
        clipboard = clipboard.splitlines()

        return clipboard

    def formatter(self, clipboard: list):
        def formatlat(latitude: str):
            latitude = latitude.replace('°', '').replace('\'', '').replace('\"', '').replace('Latitude:', '').replace(' ', '')
            
            return latitude
        
        def formatlon(longitude: str):
            longitude = longitude.replace('°', '').replace('\'', '').replace('\"', '').replace('Longitude:', '').replace(' ', '')
            
            return longitude
        
        def formatalt(altitude: str):
            real_altitude = list()

            altitude = altitude.replace('Altitude:','').replace(' ','')

            for char in altitude:
                real_altitude.append(char)
                if char == 'T':
                    print('hi')
                    break
            print(real_altitude)
            real_altitude = ''.join(real_altitude)
            real_altitude = real_altitude.replace('FT','')
            altitude = real_altitude

            return altitude

        for line in clipboard:
            if not line.find('Latitude:'):
                latitude = formatlat(line)
            if not line.find('Longitude:'):
                longitude = formatlon(line)
            if not line.find('Altitude:'):
                altitude = formatalt(line)
        
        return latitude, longitude, altitude

    def dmstomgrs(self, latitude: str, longitude: str):
        utm = mgrs.MGRS()
        latitude = utm.dmstodd(latitude)
        longitude = utm.dmstodd(longitude)
        fmgrs = utm.toMGRS(latitude, longitude, MGRSPrecision=5)
        fmgrs = fmgrs.decode('utf-8')

        return fmgrs
