

class Object:

    def __init__(self, name, description, parent):
        self._name = name
        self._description = description
        self._parent = parent

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_parent(self):
        return self._parent
