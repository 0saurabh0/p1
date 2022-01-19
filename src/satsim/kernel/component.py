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
        self.simulator = None
        self.receiver = None
        self.logger = None
        self.link_registry = None
        self.scheduler = None
        self.time_keeper = None
        self._state = self.CREATED

    def get_state(self):
        return self._state

    def _publish(self, receiver):
        """Publish all publishable fields, properties, and operations."""
        if self._state != self.CREATED:
            raise satsim.InvalidComponentState()
        self.receiver = receiver
        self.publish()
        self._state = self.PUBLISHING

    def _configure(self, logger, link_registry):
        """Perform initial configuration."""
        if self._state != self.PUBLISHING:
            raise satsim.InvalidComponentState()
        self.logger = logger
        self.link_registry = link_registry
        self.configure()
        self._state = self.CONFIGURED

    def _connect(self, simulator):
        """Connect to the simulator environment and other components."""
        if self._state != self.CONFIGURED:
            raise satsim.InvalidComponentState()
        self.simulator = simulator
        self.scheduler = simulator.get_scheduler()
        self.time_keeper = simulator.get_time_keeper()
        self.connect()
        self._state = self.CONNECTED

    def _disconnect(self):
        """Disconnect from the simulation environment and other components."""
        if self._state != self.CONNECTED:
            raise satsim.InvalidComponentState()
        self.disconnect()
        self._state = self.DISCONNECTED

    def publish(self):
        # override with custom code...
        pass

    def configure(self):
        # override with custom code...
        pass

    def connect(self):
        # override with custom code...
        pass

    def disconnect(self):
        # override with custom code...
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
