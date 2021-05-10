import satsim
from satsim import Object


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
        """Publish all publishable fields, properties, and operations."""
        if self.state != self.CREATED:
            raise satsim.InvalidComponentState()

        # custom code here

        self.state = self.PUBLISHING

    def configure(self, logger, link_registry):
        """Perform initial configuration."""
        if self.state != self.PUBLISHING:
            raise satsim.InvalidComponentState()

        # custom code here

        self.state = self.CONFIGURED

    def connect(self, simulator):
        """Connect to the simulator environment and other components."""
        if self.state != self.CONFIGURED:
            raise satsim.InvalidComponentState()

        # custom code here

        self.state = self.CONNECTED

    def disconnect(self):
        """Disconnect from the simulation environment and other components."""
        if self.state != self.CONNECTED:
            raise satsim.InvalidComponentState()

        # custom code here

        self.state = self.DISCONNECTED

    def get_field(self, full_name):
        # TODO
        raise NotImplementedError

    def get_fields(self):
        # TODO
        raise NotImplementedError

    def get_uuid(self):
        # TODO
        raise NotImplementedError
