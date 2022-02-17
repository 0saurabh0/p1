from .object import Object


class ContainerFull(Exception):
    pass


class DuplicateName(Exception):
    pass


class CannotDelete(Exception):
    pass


class NotContained(Exception):
    pass


class Container(Object):

    def __init__(self, name, description="", parent=None):
        super().__init__(name, description, parent)
        self._components = []
        self._max_count = None
        self._min_count = None

    def get_component(self, name):
        for component in self._components:
            if component.get_name() == name:
                return component
        else:
            return None

    def get_components(self):
        return self._components

    def add_component(self, component):
        if self._max_count is not None:
            if len(self._components) >= self._max_count:
                raise ContainerFull()

        for _component in self._components:
            if _component.get_name() == component.get_name():
                raise DuplicateName()

        self._components.append(component)

    def get_count(self):
        return len(self._components)

    def get_upper(self):
        return self._max_count if self._max_count is not None else -1

    def get_lower(self):
        return self._min_count if self._min_count is not None else -1

    def delete_component(self, component):
        if self._min_count is not None:
            if len(self._components) <= self._min_count:
                raise CannotDelete()

        for _component in self._components:
            if _component.get_name() == component.get_name():
                self._components.remove(component)
                return
        else:
            raise NotContained()
