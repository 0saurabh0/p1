from satsim import Service, Logger


class LinkRegistry(Service, Logger):

    def __init__(self):
        super(LinkRegistry, self).__init__()
        # Can we do it by doing a list of list?
        self.link_list = []

    def add_link(self, source, target):
        """.

        The AddLink method shall increment the link count between two
        components
        """
        # If it isn't a link before it's created or the count is 0
        # and all the possible links are in the list?
        for i in range(len(self.link_list)):
            if (self.link_list[i][0] == source
               and self.link_list[i][1] == target):
                self.link_list[i][2] += 1
                # self.log_info(self, "A new link has been created")

    def get_link_count(self, source, target):
        """.

        The GetLinkCount method shall return the link count
        between the given source and target.
        """
        for i in range(len(self.link_list)):
            if (self.link_list[i][0] == source
               and self.link_list[i][1] == target):
                return self.link_list[i][2]

    def remove_link(self, source, target):
        """.

        The RemoveLink method shall decrement the link count
        between the two components
        """
        for i in range(len(self.link_list)):
            if (self.link_list[i][0] == source
               and self.link_list[i][1] == target):
                if self.link_list[i][2] != 0:
                    self.link_list[i][2] -= 1
                    # self.logger.log_info(self, "A link has been removed")
                    return True
                if self.link_list[i][2] == 0:
                    return False

    def get_link_sources(self, target):
        """.

        The ILinkRegistry GetLinkSources method shall return the collection of
        source components for which a link to the given target component has
        been added to the registry.
        """
        for _source, _target, _link in self.link_list:
            if target == _target and _link > 0:
                return _source

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
