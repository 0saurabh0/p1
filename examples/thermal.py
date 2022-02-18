import satsim


class HotObject(satsim.Component):

    def configure(self):
        """Perform initial configuration."""
        # override with custom code...
        pass


class HotObjects(satsim.Container):

    def get_hot_object(self, alias):
        return self.get_component(alias)


class ThermalNetwork(satsim.Component, satsim.Composite):

    def configure(self):
        """Perform initial configuration."""
        # override with custom code...
        pass

    def connect(self):
        """Connect to the simulator environment and other components."""
        # override with custom code...
        pass

    def clear_network(self):
        pass

    def add_thermal_node(self, thermal_node):
        pass

    def add_hot_object(self, hot_object):
        self._containers['HOT_OBJECTS']

    def do_update(self):
        pass


thermal_network = ThermalNetwork("TNET", "My thermal network")
thermal_network.load_configuration({
    "hot_objects":,

})

ho_1 = HotObject("HO1", "", thermal_network)
thermal_network.add_hot_object(ho_1)

root = thermal_network
