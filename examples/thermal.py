import satsim


class ThermalNetwork(satsim.Component, satsim.Composite):

    def __init__(self, name, description, parent=None):
        super().__init__(name, description, parent)

        self.delta_time = None
        self.update_event_id = None

        self.update_entrypoint = satsim.EntryPoint(
            "Update",
            "Updates temperatures of all thermal nodes in the thermal network.",
            self,
            self.update
            )

        self._containers = [
            satsim.Container(
                "ThermalNodes",
                "Container for the thermal nodes of the thermal network.",
                self),
            satsim.Container(
                "HotObjects",
                "Container for the hot objects of the thermal network.",
                self)
        ]

    def add_thermal_nodes(self, thermal_nodes):
        for thermal_node in thermal_nodes:
            self.get_container('ThermalNodes').add_component(thermal_node)

    def add_hot_objects(self, hot_objects):
        for hot_object in hot_objects:
            self.get_container('HotObjects').add_component(hot_object)

    # def get_delta_time(self):
    #     return self.delta_time
    #
    # def set_delta_time(self, value):
    #     # remove event if it exists already
    #     if self.update_event_id is not None:
    #         self.scheduler.remove_event(self.update_event_id)
    #     # schedule update if delta time not zero
    #     self.delta_time = value
    #     if self.delta_time > 0:
    #         self.update_event_id = self.scheduler.add_simulation_time_event(
    #             entry_point=self.update_entrypoint,
    #             simulation_time=0,
    #             cycle_time=self.delta_time,
    #             repeat=-1)

    # def get_hot_object(self, name):
    #     raise NotImplementedError
    #
    # def get_thermal_node(self, name):
    #     raise NotImplementedError

    # def update_network(self, delta_time=None):
    #     # updates the temperature of all thermal nodes in the network
    #     raise NotImplementedError
    #
    # def update_network_with_time(self, sim_time):
    #     raise NotImplementedError
    #
    # def load_config(self, filename):
    #     raise NotImplementedError

    def update(self):
        # updates all temperatures of all thermal nodes in the thermal network
        sim_time = self.time_keeper.get_simulation_time()
        for tn in self.get_container('ThermalNodes').get_components():
            tn.update_temperature(self.delta_time)

    def publish(self):
        self.receiver.publish_field(
            "delta_time",
            "Delta time (in seconds) between two updates.",
            self.delta_time)

        self.receiver.publish_field(
            "update_event_id",
            "Event Id of cyclic update event from self-registration.",
            self.update_event_id)

    def configure(self):
        pass

    def connect(self):
        # TODO: connect thermal nodes to hot objects
        if self.delta_time > 0:
            self.update_event_id = self.scheduler.add_simulation_time_event(
                entry_point=self.update_entrypoint,
                simulation_time=0,
                cycle_time=self.delta_time,
                repeat=-1)


# thermal_node.py


class ThermalNode(satsim.Component, satsim.Composite):

    def __init__(self, name, description, parent=None):
        super().__init__(name, description, parent)

        self.base_temperature = None
        self.steady_state_temperature = None
        self.current_temperature = None
        self.rise_rate = None
        self.fall_rate = None
        self.offset = None
        self.scale = None

        self._containers = [
            satsim.Container(
                "RelatedHotObjects",
                "Container for the hot objects of the thermal network.",
                self)
        ]

    # def get_temperature(self):
    #     pass
    #
    # def set_temperature(self, value):
    #     pass

    def update_temperature(self, delta_time):
        self.steady_state_temperature = self.base_temperature
        # go through related hot objects
        # steady_state_temperature += ho.get_maximum_effect()

        if self.current_temperature < self.steady_state_temperature:
            new_temperature =\
                self.current_temperature + (self.rise_rate * delta_time)
            if new_temperature > self.steady_state_temperature:
                new_temperature = self.steady_state_temperature
        else:
            new_temperature =\
                self.current_temperature - (self.fall_rate * delta_time)
            if new_temperature < self.steady_state_temperature:
                new_temperature = self.steady_state_temperature

        self.current_temperature = new_temperature
        print(new_temperature)

    def publish(self):
        self.receiver.publish_field(
            "base_temperature",
            "Base temperature (in C) of thermal node.",
            self.base_temperature)

        self.receiver.publish_field(
            "steady_state_temperature",
            "Steady state temperature (in C) of the thermal node.",
            self.steady_state_temperature)

        self.receiver.publish_field(
            "current_temperature",
            "Current temperature (in C) of thermal node.",
            self.current_temperature)

        self.receiver.publish_field(
            "rise_rate",
            "Temperature rise rate (in C/s) of the thermal node.",
            self.rise_rate)

        self.receiver.publish_field(
            "fall_rate",
            "Temperature fall rate (in C/s) of the thermal node.",
            self.fall_rate)

        self.receiver.publish_field(
            "offset",
            "Temperature offset (in C) of the thermal node.",
            self.offset)

        self.receiver.publish_field(
            "scale_factor",
            "Temperature scale factor of the thermal node.",
            self.scale_factor)

    def configure(self):
        pass

    def connect(self):
        pass


# hot_object.py


# factory.py

def create_thermal_network(
        name, description, parent=None,
        delta_time=0):
    thermal_network = ThermalNetwork(name, description, parent)
    thermal_network.delta_time = delta_time
    return thermal_network


def create_thermal_node(
        name, description, parent=None,
        base_temperature=20,
        current_temperature=25,
        rise_rate=1,
        fall_rate=1,
        offset=0,
        scale=1):
    thermal_node = ThermalNode(name, description, parent)
    thermal_node.base_temperature = base_temperature
    thermal_node.current_temperature = current_temperature
    thermal_node.rise_rate = rise_rate
    thermal_node.fall_rate = fall_rate
    thermal_node.offset = offset
    thermal_node.scale = scale
    return thermal_node


# def create_hot_object(
#         name, description, parent=None,
#         ):
#     hot_object = HotObject(name, description, parent)
#     return hot_object


def set_related_hot_objects(thermal_node, hot_objects):
    for hot_object in hot_objects:
        thermal_node.add_related_hot_object(hot_object)


###############################################################################


thermal_network = create_thermal_network(
    "TNET", "MyTNET", None,
    delta_time=1)

TN_1 = create_thermal_node("TN_1", "", thermal_network)
#HO_1 = create_hot_object("HO_1", "", thermal_network)

#set_related_hot_objects(TN_1, [HO_1])

thermal_network.add_thermal_nodes([TN_1])
#thermal_network.add_hot_objects([HO_1])
root = thermal_network
