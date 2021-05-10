from satsim import Object


class Composite(Object):

    def get_container(self, name):
        for container in self.containers:
            if container.name == name:
                return container
        else:
            return None

    def get_containers(self):
        return self.containers
