from .object import Object


class NotReferenced(Exception):
    pass


class Reference(Object):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)
        self._components = []

    def get_component(self, name):
        for component in self._components:
            if component.get_name() == name:
                return component
        return None

    def get_components(self):
        return self._components

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        if component not in self._components:
            raise NotReferenced
        self._components.remove(component)

    def get_count(self):
        raise NotImplementedError

    def get_upper(self):
        raise NotImplementedError

    def get_lower(self):
        raise NotImplementedError
