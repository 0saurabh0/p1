from .thermal_network import ThermalNetwork
from .thermal_node import ThermalNode, RelatedHotObject
from .hot_object import HotObject


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


def create_related_hot_object(
        name, description, parent,
        hot_object,
        maximum_effect):
    related_hot_object = RelatedHotObject(name, description, parent)
    related_hot_object._hot_object = hot_object
    related_hot_object._maximum_effect = maximum_effect
    return related_hot_object
