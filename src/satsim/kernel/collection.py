from .object import Object


class Collection(Object):

    def at(self, index_or_name):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError
