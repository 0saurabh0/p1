import satsim


class HotObject(satsim.Component):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)

        self._status = None

    def get_status(self):
        return self._status

    def set_status(self, value):
        self._status = value

    def publish(self):
        self.receiver.publish_field(
            "status",
            "Status of the hot object.",
            self._status)


class HotObjects(satsim.Component, satsim.Container):
    pass
