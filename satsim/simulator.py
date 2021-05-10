from satsim import InvalidSimulatorState
from satsim import Logger, TimeKeeper, EventManager, Scheduler, Resolver,\
    LinkRegistry
from satsim import Component, Composite, Container, Publication


class Simulator(Composite, Publication):

    BUILDING = 0
    CONNECTING = 1
    INITIALISING = 2
    STANDBY = 3
    EXECUTING = 4
    STORING = 5
    RESTORING = 6
    RECONNECTING = 7
    EXITING = 8
    ABORTING = 9

    def __init__(self):
        self.containers = [
            Container("Models", "", self),
            Container("Services", "", self)
        ]

        # services
        self.logger = Logger(self)
        self.time_keeper = TimeKeeper(self)
        self.scheduler = Scheduler(self)
        self.event_manager = EventManager(self)
        self.resolver = Resolver(self)
        self.link_registry = LinkRegistry(self)

        self.init_entry_points = []

        self.state = self.BUILDING

    def publish(self):
        if self.state != self.BUILDING:
            return

        for service in self.get_container("Services").get_components():
            if service.state == Component.CREATED:
                service.publish(self)
                # TODO: call publish on all child components recursevly

        for model in self.get_container("Models").get_components():
            if model.state == Component.CREATED:
                model.publish(self)
                # TODO: call publish on all child components recursevly

    def configure(self):
        if self.state != self.BUILDING:
            return

        for service in self.get_container("Services").get_components():
            if service.state == Component.CREATED:
                service.publish(self)
            if service.state == Component.PUBLISHING:
                service.configure(self.logger, self.link_registry)
            # TODO: do this all child components recursevly

        for model in self.get_container("Models").get_components():
            if model.state == Component.CREATED:
                model.publish(self)
            if model.state == Component.PUBLISHING:
                model.configure(self.logger, self.link_registry)
            # TODO: do this all child components recursevly

    def connect(self):
        if self.state != self.BUILDING:
            return

        self.state = self.CONNECTING

        for service in self.get_container("Services").get_components():
            if service.state == Component.CREATED:
                service.publish(self)
            if service.state == Component.PUBLISHING:
                service.configure(self.logger, self.link_registry)
            if service.state == Component.CONFIGURED:
                service.connect(self)
            # TODO: do this all child components recursevly

        for model in self.get_container("Models").get_components():
            if model.state == Component.CREATED:
                model.publish(self)
            if model.state == Component.PUBLISHING:
                model.configure(self.logger, self.link_registry)
            if model.state == Component.CONFIGURED:
                model.connect(self)
            # TODO: do this all child components recursevly

        event_id = self.event_manager.query_event_id("LEAVE_CONNECTING")
        self.event_manager.emit(event_id)

        self.state = self.INITIALISING

        event_id = self.event_manager.query_event_id("ENTER_INITIALISING")
        self.event_manager.emit(event_id)

        for init_entry_point in self.init_entry_points:
            init_entry_point()
        self.init_entry_points = []

        event_id = self.event_manager.query_event_id("LEAVE_INITIALISING")
        self.event_manager.emit(event_id)

        self.state = self.STANDBY

        event_id = self.event_manager.query_event_id("ENTER_STANDBY")
        self.event_manager.emit(event_id)

    def initialise(self):
        if self.state != self.STANDBY:
            return

        event_id = self.event_manager.query_event_id("LEAVE_STANDBY")
        self.event_manager.emit(event_id)

        self.state = self.INITIALISING

        event_id = self.event_manager.query_event_id("ENTER_INITIALISING")
        self.event_manager.emit(event_id)

        for init_entry_point in self.init_entry_points:
            init_entry_point()
        self.init_entry_points = []

        event_id = self.event_manager.query_event_id("LEAVE_INITIALISING")
        self.event_manager.emit(event_id)

        self.state = self.STANDBY

        event_id = self.event_manager.query_event_id("ENTER_STANDBY")
        self.event_manager.emit(event_id)

    def run(self):
        if self.state != self.STANDBY:
            return

        event_id = self.event_manager.query_event_id("LEAVE_STANDBY")
        self.event_manager.emit(event_id)

        self.state = self.EXECUTING

        event_id = self.event_manager.query_event_id("ENTER_EXECUTING")
        self.event_manager.emit(event_id)

    def hold(self, immediate=False):
        pass

    def store(self, filename):
        pass

    def restore(self, filename):
        pass

    def reconnect(self, root):
        pass

    def exit(self):
        pass

    def abort(self):
        pass

    def get_state(self):
        pass

    def add_init_entry_point(self, entry_point):
        if self.state not in [self.BUILDING, self.CONNECTING, self.STANDBY]:
            return

        self.init_entry_points.append(entry_point)

    def add_model(self, model):
        if self.state not in [
                self.STANDBY, self.BUILDING,
                self.CONNECTING, self.INITIALISING]:
            raise InvalidSimulatorState()
        # TODO: check for conflict of name with already added model
        # TODO: check for conflict of name with already added service
        self.get_container("Models").add_component(model)

    def add_service(self, service):
        if self.state not in self.BUILDING:
            raise InvalidSimulatorState()
        # TODO: check for conflict of name with already added model
        # TODO: check for conflict of name with already added service
        self.services.append(service)

    def get_service(self, name):
        pass

    def get_logger(self):
        return self.logger

    def get_time_keeper(self):
        # TODO
        pass

    def get_scheduler(self):
        return self.scheduler

    def get_event_manager(self):
        # TODO
        pass

    def get_resolver(self):
        # TODO
        pass

    def get_link_registry(self):
        # TODO
        pass

    # def register_factory(self, component_factory):
    #     pass
    #
    # def create_instance(self, uuid, name, description, parent):
    #     pass
    #
    # def get_factory(self, uuid):
    #     pass
    #
    # def get_factories(self):
    #     pass
    #
    # def get_type_registry(self):
    #     pass
    #
    # def load_library(self, library_path):
    #     pass
