from simulator.models.basic.service import Service


class Logger(Service):

    INFORMATION = 0
    EVENT = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4

    def __init__(self):
        pass

    def log(self, sender, message, kind=None):
        pass
