from models.basic.composite import Composite


class Simulator(Composite):

    def __init__(self):
        self.models = []
        self.service = []

    def initialise(self):
        pass

    def publish(self):
        pass

    def configure(self):
        pass

    def connect(self):
        pass

    def hold(self, immediate=False):
        pass

    def store(self, filename):
        pass

    def restore(self, filename):
        pass

    def reconnect(self, root):
        pass

    def abort(self):
        pass

    def get_state(self):
        pass

    def add_init_entry_point(self, entry_point):
        pass

    def add_model(self, model):
        pass

    def add_service(self, service):
        pass

    def get_service(self, name):
        pass

    def get_logger(self):
        pass

    def get_time_keeper(self):
        pass

    def get_scheduler(self):
        pass

    def get_event_manager(self):
        pass

    def get_resolver(self):
        pass

    def get_link_registry(self):
        pass

    def register_factory(self, component_factory):
        pass

    def create_instance(self, uuid, name, description, parent):
        pass

    def get_factory(self, uuid):
        pass

    def get_factories(self):
        pass

    def get_type_registry(self):
        pass

    def load_library(self, library_path):
        pass
