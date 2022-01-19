from satsim import Service


class Logger(Service):

    INFORMATION = "INFORMATION"
    EVENT = "EVENT"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

    def __init__(self, simulator):
        self._simulator = simulator

    def log(self, sender, message, kind=None):
        print("{} | {}".format(kind, message))

    def log_info(self, sender, message):
        self.log(sender, message, kind=self.INFORMATION)

    def log_event(self, sender, message):
        self.log(sender, message, kind=self.EVENT)

    def log_warning(self, sender, message):
        self.log(sender, message, kind=self.WARNING)

    def log_error(self, sender, message):
        self.log(sender, message, kind=self.ERROR)

    def log_debug(self, sender, message):
        self.log(sender, message, kind=self.DEBUG)
