from ..service import Service


class TimeKeeper(Service):

    def __init__(self, simulator):
        self._simulator = simulator

        self._epoch_time = None
        self._mission_start_time = None
        self._mission_time = None
        self._simulation_time = None
        self._zulu_time = None

    def set_epoch_time(self, epoch_time):
        self._epoch_time = epoch_time
        self._simulator.get_event_manager().emit(14)

    def get_epoch_time(self):
        return self._epoch_time

    def set_mission_start_time(self):
        pass

    def get_mission_start_time(self):
        return self.mission_start_time

    def set_mission_time(self, ):
        pass

    def get_mission_time(self):
        return self.mission_time

    def set_simulation_time(self, simulation_time):
        self._simulation_time = simulation_time

    def get_simulation_time(self):
        return self._simulation_time

    def get_zulu_time(self):
        return self.zulu_time

    def update(self):
        # called in repsonse to scheduler executing a new event
        pass
