import satsim.generic.models.thermal as satsim


thermal_network = satsim.create_thermal_network(
    "TNET", "MyTNET", None,
    delta_time=1)

hot_objects = satsim.HotObjects("HotObjects", "", thermal_network)
HO_1 = satsim.create_hot_object(
    "HO_1", "", hot_objects,
    status=True)
hot_objects.add_component(HO_1)
thermal_network.add_container(hot_objects)

thermal_nodes = satsim.ThermalNodes("ThermalNodes", "", thermal_network)
TN_1 = satsim.create_thermal_node(
    "TN_1", "", thermal_nodes,
    base_temperature=20,
    current_temperature=25,
    rise_rate=1,
    fall_rate=1,
    offset=0,
    scale=1)
thermal_nodes.add_component(TN_1)
thermal_network.add_container(thermal_nodes)

related_hot_objects = satsim.RelatedHotObjects("RelatedHotObjects", "", TN_1)
TN_1_HO_1 = satsim.create_related_hot_object(
    "TN_1_HO_1", "", related_hot_objects,
    HO_1,
    20)
related_hot_objects.add_component(TN_1_HO_1)
TN_1.add_container(related_hot_objects)


root = thermal_network
