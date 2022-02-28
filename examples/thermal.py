import satsim


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

    def add_hot_objects(self, hot_objects):
        self._containers.append(hot_objects)

    def add_thermal_nodes(self, thermal_nodes):
        self._containers.append(thermal_nodes)

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


# thermal_node.py


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

    def add_related_hot_objects(self, related_hot_objects):
        self._containers.append(related_hot_objects)

    def get_temperature(self):
        return self._current_temperature

    def set_temperature(self, value):
        self._current_temperature = value

    def update_temperature(self, delta_time):
        self._steady_state_temperature = self._base_temperature

        for container in self._containers:
            if isinstance(container, RelatedHotObjects):
                for rel_ho in container.get_components():

        for ho in self.get_container(RELATED_HOT_OBJECTS).get_components():
            if ho.get_status() is True:
                self._steady_state_temperature += ho.get_maximum_effect()

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


class ThermalNodes(satsim.Component, satsim.Composite):
    pass


class RelatedHotObject(satsim.Component):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)

        self._hot_object_name = None
        self._maximum_effect = None


class RelatedHotObjects(satsim.Component, satsim.Composite):
    pass


# hot_object.py


class HotObject(satsim.Component):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)

        self._status = None

    def get_status(self):
        return self._status

    def set_status(self, value):
        self._status = value

    def publish(self):
        self.receiver.publish_field(
            "status",
            "Status of the hot object.",
            self._status)


class HotObjects(satsim.Component, satsim.Composite):
    pass


# factory.py


def create_thermal_network(
        name, description, parent,
        delta_time):
    thermal_network = ThermalNetwork(name, description, parent)
    thermal_network._delta_time = delta_time
    return thermal_network


def create_thermal_node(
        name, description, parent,
        base_temperature,
        current_temperature,
        rise_rate,
        fall_rate,
        offset,
        scale):
    thermal_node = ThermalNode(name, description, parent)
    thermal_node._base_temperature = base_temperature
    thermal_node._current_temperature = current_temperature
    thermal_node._rise_rate = rise_rate
    thermal_node._fall_rate = fall_rate
    thermal_node._offset = offset
    thermal_node._scale = scale
    return thermal_node


def create_hot_object(
        name, description, parent,
        status):
    hot_object = HotObject(name, description, parent)
    hot_object._status = status
    return hot_object


def set_related_hot_objects(thermal_node, hot_objects):
    for hot_object in hot_objects:
        thermal_node.add_related_hot_object(hot_object)


###############################################################################


thermal_network = create_thermal_network(
    "TNET", "MyTNET", None,
    delta_time=1)

hot_objects = HotObjects("HotObjects", "", thermal_network)

HO_1 = create_hot_object(
    "HO_1", "", hot_objects,
    status=True)
HO_2 = create_hot_object(
    "HO_2", "", hot_objects,
    status=True)

hot_objects.add_component(HO_1)
hot_objects.add_component(HO_2)

thermal_nodes = ThermalNodes("ThermalNodes", "", thermal_network)

TN_1 = create_thermal_node(
    "TN_1", "", thermal_nodes,
    base_temperature=20,
    current_temperature=25,
    rise_rate=1,
    fall_rate=1,
    offset=0,
    scale=1)
TN_2 = create_thermal_node(
    "TN_2", "", thermal_nodes,
    base_temperature=20,
    current_temperature=25,
    rise_rate=1,
    fall_rate=1,
    offset=0,
    scale=1)

thermal_nodes.add_component(TN_1)
thermal_nodes.add_component(TN_2)

REL_HO_1 = RelatedHotObject("RelatedHotObject"
#set_related_hot_objects(TN_1, [HO_1])

thermal_network.add_hot_objects(hot_objects)
thermal_network.add_thermal_nodes(thermal_nodes)
root = thermal_network
