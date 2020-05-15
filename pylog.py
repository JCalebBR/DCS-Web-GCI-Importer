import logging
import random


class Logger:
    def __init__(self):
        self.log = logging.getLogger(f'log-{random.randrange(1000,9000)}')
        self.log.setLevel(logging.DEBUG)
        self.f = '%(asctime)s :: %(levelname)s :: %(message)s : %(name)s'
        self.log.handlers.clear()
        self.console = logging.StreamHandler()
        self.formatter = logging.Formatter(self.f)
        self.console.setFormatter(self.formatter)
        self.log.addHandler(self.console)
        self.console.flush()

    def debug(self, log):
        return self.log.debug(log)