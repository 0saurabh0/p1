""" Counter Example
    This example is taken from SMP 2.0 Handbook, chapter 3
"""
from satsim import Simulator, Model, EntryPoint
simulator = Simulator()

EVENT_ENTER_STANDBY = "event enter standby"


class CounterModel(Model):

    def __init__(self, ):
        super(Model).__init__()
        self.logger = None
        self.scheduler = None
        self.count_entrypoint = EntryPoint()
        self.count_entrypoint.execute = lambda: self.count()

    def reset(self):
        self._counter = 0

    def count(self):
        self._counter += 1
        self.logger.log_info(self, "Increase counter")

    def get_counter(self):
        return self._counter

    def _publish(self, receiver):
        receiver.publish_field("counter", "Counter state", self.counter)

    def _configure(self, logger, link_registry):
        pass

    def _connect(self, simulator):
        self.logger = simulator.get_logger()
        self.scheduler = simulator.get_scheduler()
        self.scheduler.add_simulation_time_event(self.count_entrypoint, 0, 1e9)

    def _disconnect(self):
        pass


# Create model instance
counter_model = CounterModel("Counter", "Counter Model", simulator)

# Add to models container
simulator.add_model(counter_model)

simulator.publish()
simulator.configure()
simulator.connect()
simulator.initialise()
