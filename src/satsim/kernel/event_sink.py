from .object import Object


class EventSink(Object):

    def get_event_arg_type(self):
        raise NotImplementedError

    def notify(self, sender, arg):
        raise NotImplementedError
