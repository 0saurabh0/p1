from simulator.models.basic.object import Object


class CoordinateSystem(Object):

    def __init__(self):
        self.index = None
        self.parent = None
        self.position = None
        self.rotation = None
        self.root = None

    def get_matrix_to(self, coordinate_system):
        pass

    def get_matrix_from(self, coordinate_system):
        pass

    def transform_direction(self, direction):
        pass

    def transform_position(self, position):
        pass

    def transform_rotation(self, rotation):
        pass

    def get_last_update(self):
        pass


class DynamicCoordinateSystem(CoordinateSystem):
    pass
