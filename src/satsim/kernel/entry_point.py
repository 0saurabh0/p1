from .object import Object


class EntryPoint(Object):

    def __init__(self, name, description="", parent=None, function=None):
        self._name = name
        self._function = function

    def execute(self):
        self._function()
