# collection: allow to collect SMP elements in a collection

from satsim import Object


class Collection(Object):

    def __init__(self):
        pass

    def collection_at(self, index_or_name):
        """ shall return the element with the given position or name,
        if no element exists with the given position or name, it returns None
        """
        pass

    def collection_size(self):
        """ shall return the number of items in the collection
        """
        pass
