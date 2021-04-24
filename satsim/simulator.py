from satsim import InvalidSimulatorState
from satsim import Logger, TimeKeeper, EventManager, Scheduler
from satsim import Component, Composite, Publication


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
        self.models = []
        self.services = []

        # services
        self.logger = Logger(self)
        self.time_keeper = TimeKeeper(self)
        self.scheduluer = Scheduler(self)
        self.event_manager = EventManager(self)
        #self.resolver = Resolver()
        #self.link_registry = LinkRegistry()

        self.state = self.BUILDING

    def publish(self):
        """The simulator publish method shall call the `publish()` method of all
        service and model instances in the component hierarchy that are in
        `CREATED` state within the simulation.
        """

        # If simulation is not in `BUILDING` state then return without action
        if self.state != self.BUILDING:
            return

        # If execution of global even `LEAVING_BUILDING` then
        # return without action
        #TODO...

        # TODO: issue global event "Leaving Building" and wait for return

        #self.state = self.PUBLISHING

        # TODO: issue global event "EnterPublishing" and wait for return

        for service in self.services:
            if service.state == Component.CREATED:
                service.publish(self)
                # TODO: call publish on all child components recursevly

        for model in self.models:
            if model.state == Component.CREATED:
                model.publish(self)
                #TODO: call publish on all child components recursevly

        # TODO: issue global event "LeavingPublishing" and wait for return
        self.state = self.BUILDING
        # TODO: issue global event "EnterBuilding" and wait for return

    def configure(self):
        if self.state != self.BUILDING:
            return

        # TODO: if called during global event "LeavingBuilding" then return

        # TODO: issue global event "LeavingBuilding" and wait

    def connect(self):
        pass

    def initialise(self):
        pass

    def run(self):
        pass

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
        pass

    def add_model(self, model):
        if self.state not in [
                self.STANDBY, self.BUILDING,
                self.CONNECTING, self.INITIALISING]:
            raise InvalidSimulatorState()
        # TODO: check for conflict of name with already added model
        # TODO: check for conflict of name with already added service
        self.models.append(model)

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
        # TODO
        pass

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
