from .object import Object


class Persist(Object):

    def restore(self, reader):
        raise NotImplementedError

    def store(self, writer):
        raise NotImplementedError
