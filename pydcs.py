import logging
import socket
from time import sleep

from pylog import Logger


class DCS:
    def __init__(self, host='127.0.0.1', port=7778):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port
        self.log = Logger()

    def keypress(self, key, model='CDU_ANU', delay_r=0.1, delay_a=0.1):
        model_ = {'UFC': 'UFC_',
                  'CDU_ANU': 'CDU_',
                  'CDU_LSK': 'CDU_LSK_'}
        self.con.sendto(f'{model_[model]}{key} 1\n'.encode(
            'utf-8'), (self.host, self.port))
        sleep(delay_r)
        self.con.sendto(f'{model_[model]}{key} 0\n'.encode(
            'utf-8'), (self.host, self.port))
        sleep(delay_a)

        self.log.debug(key)

    def close(self):
        self.con.close()
        self.log.debug("DCS Bios Connection closed")

    def mgrstodcs(self, mgrs):
        try:
            self.clearcdu()
            done = 0
            for idx, char in enumerate(mgrs):
                if (idx > 2 and done == 0):
                    self.keypress('7L', 'CDU_LSK')
                    done = 1
                self.keypress(char)
            self.keypress('9L', 'CDU_LSK')
        except TypeError as ex:
            self.log.exception(ex)

    def ddtodcs(self, lat, lon):
        self.clearcdu()
        for char in lat:
            self.keypress(char)
        self.keypress('7L', 'CDU_LSK')
        for char in lon:
            self.keypress(char)
        self.keypress('9L', 'CDU_LSK')

    def elevtodcs(self, elevation):
        try:
            self.clearcdu()
            for num in elevation:
                self.keypress(num)
            self.keypress('5L', 'CDU_LSK')
        except TypeError as ex:
            self.log.exception(ex)

    def nametodcs(self, name):
        self.clearcdu()
        name = name.upper()
        for count, char in enumerate(name):
            if count < 12:
                if char == ' ':
                    self.keypress('SPC')
                else:
                    self.keypress(char)
            else:
                break
        self.keypress('3R', 'CDU_LSK')

    def clearcdu(self):
        self.keypress('CLR')
