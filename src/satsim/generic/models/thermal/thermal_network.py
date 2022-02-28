import satsim

from .hot_object import HotObjects
from .thermal_node import ThermalNodes


class ThermalNetwork(satsim.Component, satsim.Composite):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)

        self._delta_time = None
        self._update_event_id = None

        self._update_entrypoint = satsim.EntryPoint(
            "Update",
            "Updates temperatures of all thermal nodes in the thermal network.",
            self,
            self.update
            )

        self._containers = []

    def get_delta_time(self):
        return self.delta_time

    def set_delta_time(self, value):
        # remove event if it exists already
        if self.update_event_id is not None:
            self.scheduler.remove_event(self.update_event_id)
        # schedule update if delta time not zero
        self.delta_time = value
        if self.delta_time > 0:
            self.update_event_id = self.scheduler.add_simulation_time_event(
                entry_point=self.update_entrypoint,
                simulation_time=0,
                cycle_time=self.delta_time,
                repeat=-1)

    def get_hot_object(self, name):
        for container in self._containers:
            if isinstance(container, HotObjects):
                for ho in container.get_components():
                    if ho.get_name() == name:
                        return ho
        return None

    def get_thermal_node(self, name):
        for container in self._containers:
            if isinstance(container, ThermalNodes):
                for tn in container.get_components():
                    if tn.get_name() == name:
                        return tn
        return None

    # def load_config(self, filename):
    #     raise NotImplementedError

    def update(self):
        # updates all temperatures of all thermal nodes in the thermal network
        for container in self._containers:
            if isinstance(container, ThermalNodes):
                for tn in container.get_components():
                    tn.update_temperature(self._delta_time)

    def publish(self):
        self.receiver.publish_field(
            "delta_time",
            "Delta time (in seconds) between two updates.",
            self._delta_time)

    def configure(self):
        pass

    def connect(self):
        if self._delta_time > 0:
            self._update_event_id = self.scheduler.add_simulation_time_event(
                entry_point=self._update_entrypoint,
                simulation_time=0,
                cycle_time=self._delta_time,
                repeat=-1)
