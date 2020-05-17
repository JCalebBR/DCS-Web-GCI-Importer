import logging
import random
from datetime import datetime
import os

class Logger:
    def __init__(self):
        self.now = datetime.now()
        self.now = self.now.strftime('%H-%M-%S')

        self.log = logging.getLogger(f'log-{random.randrange(1000,9000)}')
        self.log.setLevel(logging.DEBUG)

        self.f = '%(asctime)s :: %(levelname)s :: %(message)s : %(name)s'
        self.formatter = logging.Formatter(self.f, datefmt='%H:%M:%S')
        
        self.console = logging.StreamHandler()
        self.console.setFormatter(self.formatter)
        self.log.addHandler(self.console)

        try:
            self.fhandler = logging.FileHandler(f'logs/log-{self.now}.log')
        except FileNotFoundError:
            os.mkdir('logs')
            self.fhandler = logging.FileHandler(f'logs/log-{self.now}.log')
        
        self.fhandler.setFormatter(self.formatter)
        self.log.addHandler(self.fhandler)

    def debug(self, msg, *args, **kwargs):
        return self.log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self.log.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self.log.warning(msg, *args, **kwargs)

    def error(self, error, *args, **kwargs):
        return self.log.error(error, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        return self.log.critical(msg, *args, **kwargs)
    
    def exception(self, exception, *args, **kwargs):
        return self.log.exception(exception, *args, **kwargs)
