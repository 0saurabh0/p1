from .object import Object


class Aggregate(Object):

    def get_reference(self, name):
        if hasattr(self, '_references'):
            for reference in self._references:
                if reference.get_name() == name:
                    return reference
        return None

    def get_references(self):
        if hasattr(self, '_references'):
            return self._references
        return list()
