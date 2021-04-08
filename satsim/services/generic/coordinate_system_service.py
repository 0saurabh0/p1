from simulator.models.basic.service import Service


class CoordinateSystemService(Service):

    def __init__(self):
        self.coordinate_systems = []

    def get_by_name(self, name):
        pass

    def get_by_index(self, index):
        pass

    def register(self, name, description, parent, position, rotation):
        pass

    def transfer(self, coordinate_system, parent, position, rotation):
        pass
