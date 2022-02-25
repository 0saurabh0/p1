import enum

from .object import Object


class InvalidComponentState(Exception):
    pass


class ComponentState(enum.IntEnum):
    CREATED = 0
    PUBLISHING = 1
    CONFIGURED = 2
    CONNECTED = 3
    DISCONNECTED = 4


class Component(Object):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)

        self.simulator = None
        self.receiver = None
        self.logger = None
        self.link_registry = None
        self.scheduler = None
        self.time_keeper = None

        self._state = ComponentState.CREATED

    def get_state(self):
        return self._state

    def _publish(self, receiver):
        if self._state != ComponentState.CREATED:
            raise InvalidComponentState()
        self.receiver = receiver
        self._state = ComponentState.PUBLISHING
        self.publish()

    def _configure(self, logger, link_registry):
        if self._state != ComponentState.PUBLISHING:
            raise InvalidComponentState()
        self.logger = logger
        self.link_registry = link_registry
        self.configure()
        self._state = ComponentState.CONFIGURED

    def _connect(self, simulator):
        if self._state != ComponentState.CONFIGURED:
            raise InvalidComponentState()
        self.simulator = simulator
        self.scheduler = simulator.get_scheduler()
        self.time_keeper = simulator.get_time_keeper()
        self.connect()
        self._state = ComponentState.CONNECTED

    def _disconnect(self):
        if self._state != self.CONNECTED:
            raise InvalidComponentState()
        self.disconnect()
        self._state = ComponentState.DISCONNECTED

    def publish(self):
        """Publish all publishable fields, properties, and operations."""
        # override with custom code...
        pass

    def configure(self):
        """Perform initial configuration."""
        # override with custom code...
        pass

    def connect(self):
        """Connect to the simulator environment and other components."""
        # override with custom code...
        pass

    def disconnect(self):
        """Disconnect from the simulation environment and other components."""
        # override with custom code...
        pass

    def get_field(self, full_name):
        raise NotImplementedError

    def get_fields(self):
        raise NotImplementedError

    def get_uuid(self):
        raise NotImplementedError
