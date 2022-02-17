from ..service import Service


class Resolver(Service):

    def __init__(self, simulator):
        self._simulator = simulator

    def resolve_absolute(self, absolute_path):
        raise NotImplementedError

    def resolve_relative(self, relative_path):
        raise NotImplementedError
