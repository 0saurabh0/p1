

class Object:

    def __init__(self, name, description, parent=None):
        self.name = name
        self.description = description
        self.parent = parent

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_parent(self):
        return self.parent
