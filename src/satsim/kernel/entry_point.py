from .object import Object


class EntryPoint(Object):

    def __init__(self, name, description, parent, function):
        self._name = name
        self._function = function

    def execute(self):
        self._function()
