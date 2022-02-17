from .object import Object


class EventSource(Object):

    def subscribe(self, event_sink):
        raise NotImplementedError

    def unsubscribe(self, event_sink):
        raise NotImplementedError
