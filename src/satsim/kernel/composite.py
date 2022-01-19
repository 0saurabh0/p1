from satsim import Object


class Composite(Object):

    def get_container(self, name):
        for container in self._containers:
            if container.get_name() == name:
                return container
        else:
            return None

    def get_containers(self):
        return self._containers
