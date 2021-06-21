import time

import satsim


class CounterModel(satsim.Model):

    def __init__(self, name, description, parent):
        super().__init__(name, description, parent)
        self.counter = 0
        self.count_entrypoint = satsim.EntryPoint("Increase Counter")
        self.count_entrypoint.execute = self.count
        self.reset_entrypoint = satsim.EntryPoint("Reset Counter")
        self.reset_entrypoint.execute = self.reset
        self.log_entrypoint = satsim.EntryPoint("Log Counter")
        self.log_entrypoint.execute = self.log_count
        self.log_time_entrypoint = satsim.EntryPoint("Log Time")
        self.log_time_entrypoint.execute = self.log_time

    def reset(self):
        print("Reset counter")
        self.counter = 0

    def count(self):
        # self.counter += 1
        self.counter = 2*self.time_keeper.get_simulation_time()
        print("Increase counter. Value now:", self.counter)

    def log_count(self):
        print("Log counter:", self.counter)

    def log_time(self):
        print("Current time:", self.time_keeper.get_simulation_time())

    def configure(self, logger, link_registry):
        if self._state != self.PUBLISHING:
            raise satsim.InvalidComponentState()

        self.logger = logger
        self.logger.log_info(self, "Counter Model is now configured")
        self._state = self.CONFIGURED

    def connect(self, simulator):
        if self._state != self.CONFIGURED:
            raise satsim.InvalidComponentState()

        self.simulator = simulator
        self.scheduler = simulator.get_scheduler()
        self.time_keeper = simulator.get_time_keeper()

        self.scheduler.add_simulation_time_event(self.log_time_entrypoint, 0, 1, 7)
        self.scheduler.add_simulation_time_event(self.count_entrypoint, 1, 5, 1)
        self.scheduler.add_simulation_time_event(self.log_entrypoint, 2, 1.5, 2)
        self.scheduler.add_simulation_time_event(self.reset_entrypoint, 3)

        self.logger.log_info(self, "Counter Model is now connected")
        self._state = self.CONNECTED


# create simulator
simulator = satsim.Simulator()

# create model instance
counter_model = CounterModel("Counter", "Counter Model", simulator)

# add to models container
simulator.add_model(counter_model)

# simulator starting
simulator.publish()
simulator.configure()
simulator.connect()
simulator.initialise()

print("Simulation started")
simulator.run()

# run for some time
for i in range(10):
    print("Current event:", simulator.get_scheduler().get_current_event_id())
    time.sleep(1)

print("Simulation completed")
simulator.exit()
