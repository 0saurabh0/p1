import satsim


class ThermalNode(satsim.Component, satsim.Composite):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)

        self._base_temperature = None
        self._steady_state_temperature = None
        self._current_temperature = None
        self._rise_rate = None
        self._fall_rate = None
        self._offset = None
        self._scale = None

        self._containers = []

    def get_temperature(self):
        return self._current_temperature

    def set_temperature(self, value):
        self._current_temperature = value

    def update_temperature(self, delta_time):
        self._steady_state_temperature = self._base_temperature

        maximum_effect = 0

        for container in self._containers:
            if isinstance(container, RelatedHotObjects):
                for rel_ho in container.get_components():
                    if rel_ho.get_hot_object().get_status() is True:
                        maximum_effect += rel_ho.get_maximum_effect()

        self._steady_state_temperature += maximum_effect

        if self._current_temperature < self._steady_state_temperature:
            new_temperature =\
                self._current_temperature + (self._rise_rate * delta_time)
            if new_temperature > self._steady_state_temperature:
                new_temperature = self._steady_state_temperature
        else:
            new_temperature =\
                self._current_temperature - (self._fall_rate * delta_time)
            if new_temperature < self._steady_state_temperature:
                new_temperature = self._steady_state_temperature

        self._current_temperature = new_temperature
        print(new_temperature)

    def publish(self):
        self.receiver.publish_field(
            "base_temperature",
            "Base temperature (in C) of thermal node.",
            self._base_temperature)

        self.receiver.publish_field(
            "steady_state_temperature",
            "Steady state temperature (in C) of the thermal node.",
            self._steady_state_temperature)

        self.receiver.publish_field(
            "current_temperature",
            "Current temperature (in C) of thermal node.",
            self._current_temperature)

        self.receiver.publish_field(
            "rise_rate",
            "Temperature rise rate (in C/s) of the thermal node.",
            self._rise_rate)

        self.receiver.publish_field(
            "fall_rate",
            "Temperature fall rate (in C/s) of the thermal node.",
            self._fall_rate)

        self.receiver.publish_field(
            "offset",
            "Temperature offset (in C) of the thermal node.",
            self._offset)

        self.receiver.publish_field(
            "scale_factor",
            "Temperature scale factor of the thermal node.",
            self._scale_factor)


class ThermalNodes(satsim.Component, satsim.Container):
    pass


class RelatedHotObject(satsim.Component):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)

        self._hot_object = None
        self._maximum_effect = None

    def get_hot_object(self):
        return self._hot_object

    def get_maximum_effect(self):
        return self._maximum_effect


class RelatedHotObjects(satsim.Component, satsim.Container):
    pass
