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
            self.my_publish(receiver)

    def configure(self, logger, link_registry):
        if self.state != self.PUBLISHING:
            raise InvalidComponentState()
        else:
            self.my_configure(logger, link_registry)
            self.state = self.CONFIGURED

    def connect(self, simulator):
        if self.state != self.CONFIGURED:
            raise InvalidComponentState()
        else:
            self.state = self.CONNECTED
            self.my_connect(simulator)

    def disconnect(self):
        if self.state != self.CONNECTED:
            raise InvalidComponentState()
        else:
            self.state = self.DISCONNECTED
            self.my_disconnect()

    def my_publish(self, receiver):
        """Publish all publishable fields, properties, and operations.
        To be implemented by user.
        """
        pass

    def my_configure(self, logger, link_registry):
        """Perform initial configuration.
        To be implemented by user.
        """
        pass

    def my_connect(self, simulator):
        """Connect to the simulator environment and other components.
        To be implemented by user.
        """
        pass

    def my_disconnect(self):
        """Disconnect from the simulation environment and any other component.
        To be implemented by user.
        """
        pass

    def get_field(self, full_name):
        # TODO
        raise NotImplementedError

    def get_fields(self):
        # TODO
        raise NotImplementedError

    def get_uuid(self):
        # TODO
        raise NotImplementedError
