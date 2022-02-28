from .object import Object


class Composite(Object):

    def get_container(self, name):
        if hasattr(self, '_containers'):
            for container in self._containers:
                if container.get_name() == name:
                    return container
        return None

    def get_containers(self):
        if hasattr(self, '_containers'):
            return self._containers
        return list()

    def add_container(self, container):
        self._containers.append(container)
