""" Counter Example
    This example is taken from SMP 2.0 Handbook, chapter 3
"""
import time
from datetime import timedelta

import satsim
from satsim import Simulator, Model, EntryPoint
simulator = Simulator()


class CounterModel(Model):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)
        self._counter = 0
        self._entrypoint = EntryPoint("counter entrypoint")
        self._entrypoint.execute = lambda: self._log_count()

    def _reset(self):
        self._counter = 0

    def _count(self):
        self._counter += 1
        self.logger.log_info(self, "Increase counter")

    def _log_count(self):
        self.logger.log_info(self, "Counter value {}".format(self._counter))

    def configure(self, logger, link_registry):
        """Perform initial configuration."""
        if self.state != self.PUBLISHING:
            raise satsim.InvalidComponentState()

        self.logger = logger
        self.logger.log_info(self, "Counter Model is now configured.")

        self.state = self.CONFIGURED

    def connect(self, simulator):
        """Connect to the simulator environment and other components."""
        if self.state != self.CONFIGURED:
            raise satsim.InvalidComponentState()

        self.scheduler = simulator.get_scheduler()
        self.scheduler.add_simulation_time_event(
            self._entrypoint, timedelta(seconds=1))
        self.logger.log_info(self, "Counter Model is now connected.")

        self.state = self.CONNECTED


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
