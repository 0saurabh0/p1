""" Counter Example
    This example is taken from SMP 2.0 Handbook, chapter 3
"""
import time
from datetime import timedelta

from satsim import Simulator, Model, EntryPoint
simulator = Simulator()


class CounterModel(Model):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)
        self.counter = 0
        self.my_entrypoint = EntryPoint("counter entrypoint")
        self.my_entrypoint.execute = lambda: self.log_count()

    def reset(self):
        self.counter = 0

    def count(self):
        self.counter += 1
        self.logger.log_info(self, "Increase counter")

    def log_count(self):
        self.logger.log_info(self, "Counter value {}".format(self.counter))

    # def _publish(self, receiver):
    #     receiver.publish_field("counter", "Counter state", self.counter)

    def _configure(self, logger, link_registry):
        self.logger = logger

    def _connect(self, simulator):
        self.scheduler = simulator.get_scheduler()
        self.scheduler.add_simulation_time_event(
            self.count_entrypoint, timedelta(seconds=1))

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

print("Simulation started")
simulator.run()
time.sleep(1)  # run for some time
simulator.exit()
print("Simulation finished")
