from satsim import Service


class LinkRegistry(Service):

    def __init__(self):
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
        """
        Return the source components for which a link to given target has
        been added to the registry.
        """
        sources = []
        for source, _target in self._links.keys():
            if _target == target:
                sources.append(source)
        return sources

    def can_remove(self, target):
        """.

        The ILinkRegistry CanRemove method shall return whether all source
        components linking to the given target can be asked to remove their
        link(s).
        """

        # (a) If all source components linking to the given target can be asked
        # to remove their link(s), it returns true;
        # (b) If at least one of the source components linking to the given
        # target cannot be asked to remove its link(s), it returns false.

        # I don't know how to do this

    def remove_links(self, target):
        """.

        The RemoveLinks method shall call the RemoveLinks method of all source
        components that implement the optional ILinkingComponent interface:
        """
        for _source, _target, _link in self.link_list:
            if target == _target:
                # remove_link(_source, target)
                # how to this until _link = 0?
                pass
