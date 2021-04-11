from satsim import InvalidComponentState, Object


class Component(Object):

    CREATED = 0
    PUBLISHING = 1
    CONFIGURED = 2
    CONNECTED = 3
    DISCONNECTED = 4

    def __init__(self, name, description, parent=None):
        super().__init__(name, description, parent)
        self.state = self.CREATED

    def get_state(self):
        return self.state

    def publish(self, receiver):
        if self.state != self.CREATED:
            raise InvalidComponentState()
        else:
            self.state = self.PUBLISHING
            self._publish(receiver)

    def _publish(self, receiver):
        # To be implemented by user
        pass

    def configure(self, logger, link_registry):
        if self.state != self.PUBLISHING:
            raise InvalidComponentState()
        else:
            self._configure(logger, link_registry)
            self.state = self.CONFIGURED

    def _configure(self, logger, link_registry):
        # To be implemented by user
        pass

    def connect(self, simulator):
        if self.state != self.CONFIGURED:
            raise InvalidComponentState()
        else:
            self.state = self.CONNECTED
            self._connect(simulator)

    def _connect(self, simulator):
        # To be implemented by user
        pass

    def disconnect(self):
        if self.state != self.CONNECTED:
            raise InvalidComponentState()
        else:
            self.state = self.DISCONNECTED
            self._disconnect()

    def _disconnect(self):
        # To be implemented by user
        pass

    def get_field(self, full_name):
        raise NotImplementedError

    def get_fields(self):
        raise NotImplementedError

    def get_uuid(self):
        raise NotImplementedError
