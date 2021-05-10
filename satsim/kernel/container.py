from satsim import Object


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
        self.components = []
        self.max_count = None
        self.min_count = None

    def get_component(self, name):
        for component in self.components:
            if component.name == name:
                return component
        else:
            return None

    def get_components(self):
        return self.components

    def add_component(self, component):
        if self.max_count is not None:
            if len(self.components) >= self.max_count:
                raise ContainerFull()

        for _component in self.components:
            if _component.name == component.name:
                raise DuplicateName()

        self.components.append(component)

    def get_count(self):
        return len(self.components)

    def get_upper(self):
        return self.max_count if self.max_count is not None else -1

    def get_lower(self):
        return self.min_count if self.min_count is not None else -1

    def delete_component(self, component):
        if self.min_count is not None:
            if len(self.components) <= self.min_count:
                raise CannotDelete()

        for _component in self.components:
            if _component.name == component.name:
                self.components.pop(component)
                return
        else:
            raise NotContained()
