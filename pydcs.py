import socket
from time import sleep


class DCS:
    def __init__(self, host='127.0.0.1', port=7778):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port

    def keypress(self, key, model='CDU_ANU', delay_r=0.1, delay_a=0.1):
        model_ = {'UFC':'UFC_',
                  'CDU_ANU':'CDU_',
                  'CDU_LSK':'CDU_LSK_'}
        self.con.sendto(f'{model_[model]}{key} 1\n'.encode('utf-8'), (self.host, self.port))
        sleep(delay_r)
        self.con.sendto(f'{model_[model]}{key} 0\n'.encode('utf-8'), (self.host, self.port))
        sleep(delay_a)

    def close(self):
        self.con.close()

    def mgrstodcs(self, mgrs: str):
        self.clearcdu()
        done = 0
        for idx, char in enumerate(mgrs):
            if (idx > 2 and done == 0):
                self.keypress('7L', 'CDU_LSK')
                done = 1
            self.keypress(char)
            print(char)
        self.keypress('9L', 'CDU_LSK')
    
    def elevtodcs(self, elevation: str):
        self.clearcdu()
        for num in elevation:
            self.keypress(num)
        self.keypress('5L', 'CDU_LSK')

    def nametodcs(self, name: str):
        self.clearcdu()
        for char in name:
            self.keypress(char)
        self.keypress('3R', 'CDU_LSK')

    def clearcdu(self):
        self.keypress('CLR')