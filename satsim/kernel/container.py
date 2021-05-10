from satsim import Object


class Container(Object):

    def __init__(self, name, description="", parent=None):
        super().__init__(name, description, parent)
        self.components = []
        self.max_len = -1
        self.min_len = -1

    def get_component(self, name):
        if name not in self.components:
            return None

        else:
            for _name in self.components:
                if _name == name:
                    return _name

    def get_components(self):
        """
        Return a collection of all the contained components ordered according
        to the order in which the components have been added using the
        add_component method.
        """
        return self.components

    def add_component(self, component):
        # If the maximum supported number of components is reached, it
        # throws a ContainerFull exception
        if len(self.components) == self.max_len:
            raise ContainerFull()

        # If a component with the same name and parent already exists,
        # it throws a DuplicateName exception
        elif component in self.components:
            raise DuplicateName()

        # If the container interface implementation is expecting the given
        # component to inherit from another type, it throws an
        # InvalidObjectType exception

        else:
            self.components.append(component)

    def get_count(self):
        return len(self.components)

    def get_upper(self):
        # If the maximum number of elements for the collection has been
        # defined, it returns the maximum number. If not, it returns -1.
        #if len(self.max_len) == 0:
        if self.max_len:
            return -1

        else:
            #return self.max_len[0]
            return self.max_len

    def get_lower(self):
        #if len(self.min_len) == 0:
        if self.min_len:
            return 0

        else:
            #return self.min_len[0]
            return self.min_len

    def delete_component(self, component):
        # If the minimum number of component(s) contained by this object
        # is reached, it throws a CannotDelete
        if len(self.components) == self.min_len:
            raise CannotDelete()

        elif component not in self.components:
            raise NotContained()

        else:
            self.components.remove(component)
