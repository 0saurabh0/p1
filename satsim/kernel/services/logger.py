from satsim import Service


class Logger(Service):

    INFORMATION = 0
    EVENT = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4

    def __init__(self):
        pass

    def log(self, sender, message, kind=0):
        print("{} | {} | {}".format(kind, sender, message))

    def log_info(self, sender, message):
        self.log(sender, message, kind=self.INFORMATION)
