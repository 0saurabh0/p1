import threading
import enum

import simpy.rt as sp

from .kernel import Composite, ComponentState, Container
from .kernel.services import Logger, TimeKeeper, EventManager, Scheduler,\
    Resolver, LinkRegistry


class InvalidSimulatorState(Exception):
    pass


class SimulationState(enum.IntEnum):
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


class Simulator(Composite):

    def __init__(self):
        self._containers = [
            Container("Models", "", self),
            Container("Services", "", self)
        ]
        self._logger = Logger(self)
        self._time_keeper = TimeKeeper(self)
        self._scheduler = Scheduler(self)
        self._event_manager = EventManager(self)
        self._resolver = Resolver(self)
        self._link_registry = LinkRegistry(self)

        self._init_entry_points = []

        self._env = sp.RealtimeEnvironment(factor=1, strict=False)
        self._terminate = False

        self._state = SimulationState.BUILDING

    def publish(self):
        if self._state != SimulationState.BUILDING:
            return

        for service in self.get_container("Services").get_components():
            if service._state == ComponentState.CREATED:
                service._publish(self)
                # TODO: call publish on all child components recursevly

        for model in self.get_container("Models").get_components():
            if model._state == ComponentState.CREATED:
                model._publish(self)
                # TODO: call publish on all child components recursevly

    def configure(self):
        if self._state != SimulationState.BUILDING:
            return

        for service in self.get_container("Services").get_components():
            if service._state == ComponentState.CREATED:
                service._publish(self)
            if service._state == ComponentState.PUBLISHING:
                service._configure(self._logger, self._link_registry)
            # TODO: do this all child components recursevly

        for model in self.get_container("Models").get_components():
            if model._state == ComponentState.CREATED:
                model._publish(self)
            if model._state == ComponentState.PUBLISHING:
                model._configure(self._logger, self._link_registry)
            # TODO: do this all child components recursevly

    def connect(self):
        if self._state != SimulationState.BUILDING:
            return

        self._state = SimulationState.CONNECTING

        for service in self.get_container("Services").get_components():
            if service._state == ComponentState.CREATED:
                service._publish(self)
            if service._state == ComponentState.PUBLISHING:
                service._configure(self.logger, self.link_registry)
            if service._state == ComponentState.CONFIGURED:
                service._connect(self)
            # TODO: do this all child components recursevly

        for model in self.get_container("Models").get_components():
            if model._state == ComponentState.CREATED:
                model._publish(self)
            if model._state == ComponentState.PUBLISHING:
                model._configure(self.logger, self.link_registry)
            if model._state == ComponentState.CONFIGURED:
                model._connect(self)
            # TODO: do this all child components recursevly

        event_id = self._event_manager.query_event_id("LEAVE_CONNECTING")
        self._event_manager.emit(event_id)

        self._state = SimulationState.INITIALISING

        event_id = self._event_manager.query_event_id("ENTER_INITIALISING")
        self._event_manager.emit(event_id)

        for init_entry_point in self._init_entry_points:
            init_entry_point()
        self._init_entry_points = []

        event_id = self._event_manager.query_event_id("LEAVE_INITIALISING")
        self._event_manager.emit(event_id)

        self._state = SimulationState.STANDBY

        event_id = self._event_manager.query_event_id("ENTER_STANDBY")
        self._event_manager.emit(event_id)

    def initialise(self):
        if self._state != SimulationState.STANDBY:
            return

        event_id = self._event_manager.query_event_id("LEAVE_STANDBY")
        self._event_manager.emit(event_id)

        self._state = SimulationState.INITIALISING

        event_id = self._event_manager.query_event_id("ENTER_INITIALISING")
        self._event_manager.emit(event_id)

        for init_entry_point in self._init_entry_points:
            init_entry_point()
        self._init_entry_points = []

        event_id = self._event_manager.query_event_id("LEAVE_INITIALISING")
        self._event_manager.emit(event_id)

        self._state = SimulationState.STANDBY

        event_id = self._event_manager.query_event_id("ENTER_STANDBY")
        self._event_manager.emit(event_id)

    def run(self):
        if self._state != SimulationState.STANDBY:
            return

        event_id = self._event_manager.query_event_id("LEAVE_STANDBY")
        self._event_manager.emit(event_id)

        self._state = SimulationState.EXECUTING

        event_id = self._event_manager.query_event_id("ENTER_EXECUTING")
        self._event_manager.emit(event_id)

        # start the simulation
        self._env.process(self._simulation_process())
        t = threading.Thread(target=self._env.run)
        t.start()

    def _simulation_process(self):
        self._time_keeper.set_simulation_time(0)
        while True:
            self._scheduler.current_event_id = None

            if self._terminate:
                break
            for event_id, event in sorted(
                    self._scheduler._scheduled_events.items()):

                if self._env.now >= event['simulation_time']:
                    self._scheduler.current_event_id = event_id
                    event['entry_point'].execute()
                    if event['repeat'] > 0:
                        event['repeat'] -= 1
                        event['simulation_time'] += event['cycle_time']
                    elif event['repeat'] == 0:
                        del self._scheduler._scheduled_events[event_id]
                    else:
                        event['simulation_time'] += event['cycle_time']

            simulation_time = self._time_keeper.get_simulation_time()
            self._time_keeper.set_simulation_time(simulation_time + 1)
            yield self._env.timeout(1)

    def hold(self, immediate=False):
        pass

    def store(self, filename):
        pass

    def restore(self, filename):
        pass

    def reconnect(self, root):
        pass

    def exit(self):
        self._terminate = True

    def abort(self):
        pass

    def get_state(self):
        return self._state

    def add_init_entry_point(self, entry_point):
        if self._state not in [
                SimulationState.BUILDING,
                SimulationState.CONNECTING,
                SimulationState.STANDBY]:
            return

        self.init_entry_points.append(entry_point)

    def add_model(self, model):
        if self._state not in [
                SimulationState.STANDBY,
                SimulationState.BUILDING,
                SimulationState.CONNECTING,
                SimulationState.INITIALISING]:
            raise InvalidSimulatorState()
        self.get_container("Models").add_component(model)

    def add_service(self, service):
        if self._state not in SimulationState.BUILDING:
            raise InvalidSimulatorState()
        self.services.append(service)

    def get_service(self, name):
        pass

    def get_logger(self):
        return self._logger

    def get_time_keeper(self):
        return self._time_keeper

    def get_scheduler(self):
        return self._scheduler

    def get_event_manager(self):
        return self._event_manager

    def get_resolver(self):
        return self._resolver

    def get_link_registry(self):
        return self._link_registry
