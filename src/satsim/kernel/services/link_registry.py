from ..service import Service


class LinkRegistry(Service):

    def __init__(self, simulator):
        self._simulator = simulator
        self._links = {}

    def add_link(self, source, target):
        if (source, target) not in self._links:
            self._links[(source, target)] = 1
        else:
            self._links[(source, target)] += 1

    def get_link_count(self, source, target):
        if (source, target) not in self._links:
            return 0
        else:
            return self._links[(source, target)]

    def remove_link(self, source, target):
        if (source, target) not in self._links:
            return False
        else:
            if self._links[(source, target)] > 0:
                self._links[(source, target)] -= 1
            else:
                return False

    def get_link_sources(self, target):
        sources = []
        for source, _target in self._links.keys():
            if _target == target:
                sources.append(source)
        return sources

    def can_remove(self, target):
        raise NotImplementedError

    def remove_links(self, target):
        for source, _target in self._links.keys():
            if _target == target:
                while self._links[(source, _target)] > 0:
                    self.remove_link(source, _target)
