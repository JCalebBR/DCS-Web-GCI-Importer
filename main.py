import re
from time import sleep

import keyboard
import mgrs
import pyautogui
import pyperclip

def formatter(latitude: str, longitude: str):
    latitude = latitude.replace('°', '').replace('\'', '').replace('\"', '').replace('Latitude:', '').replace(' ', '')
    longitude = longitude.replace('°', '').replace('\'', '').replace('\"', '').replace('Longitude:', '').replace(' ', '')

    return latitude, longitude

def dmstomgrs(latitude: str, longitude: str):
    utm = mgrs.MGRS()
    latitude = utm.dmstodd(latitude)
    longitude = utm.dmstodd(longitude)

    return utm.toMGRS(latitude, longitude, MGRSPrecision=5)

def clipimport():
    pyautogui.hotkey('Ctrl','Insert')
    clipboard = pyperclip.paste()
    clipboard = clipboard.splitlines()

    return clipboard

def main():
    clipboard = clipimport()
    lat, lon = formatter(clipboard[4], clipboard[5])
    fmgrs = dmstomgrs(lat, lon)
    print(fmgrs.decode('utf-8'))


keyboard.add_hotkey('Shift+C', main)
keyboard.wait('esc')
