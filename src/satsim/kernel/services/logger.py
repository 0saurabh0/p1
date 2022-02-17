import enum

from ..service import Service


class LogMessageKind(enum.Enum):
    INFORMATION = "INFORMATION"
    EVENT = "EVENT"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"


class Logger(Service):

    def __init__(self, simulator):
        self._simulator = simulator

    def log(self, sender, message, kind=None):
        print("{} | {}".format(kind, message))

    def log_info(self, sender, message):
        self.log(sender, message, kind=LogMessageKind.INFORMATION)

    def log_event(self, sender, message):
        self.log(sender, message, kind=LogMessageKind.EVENT)

    def log_warning(self, sender, message):
        self.log(sender, message, kind=LogMessageKind.WARNING)

    def log_error(self, sender, message):
        self.log(sender, message, kind=LogMessageKind.ERROR)

    def log_debug(self, sender, message):
        self.log(sender, message, kind=LogMessageKind.DEBUG)
