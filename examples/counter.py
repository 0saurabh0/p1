import time

import satsim


class Counter(satsim.Model):

    def configure(self):
        self._count = 0
        self.count_entrypoint = satsim.EntryPoint("Increase Counter", self.count)
        self.reset_entrypoint = satsim.EntryPoint("Reset Counter", self.reset)

    def connect(self):
        self.scheduler.add_simulation_time_event(self.count_entrypoint, 1, 1, 1)
        self.scheduler.add_simulation_time_event(self.reset_entrypoint, 0)
        self.logger.log_info(self, "Counter Model is now connected")

    def reset(self):
        self._count = 0

    def count(self):
        self._count += 1

    def add(self, offset):
        self._count += offset
        return self._count


# create simulator
simulator = satsim.Simulator()

# create model instance
counter = Counter("Counter", "A simple counter", simulator)

# add to models container
simulator.add_model(counter)

# simulator setup
simulator.publish()
simulator.configure()
simulator.connect()
simulator.initialise()

# start executing simulation
simulator.run()
print("Simulation running...")

# run for some time
for i in range(5):
    print("Current event:", simulator.get_scheduler().get_current_event_id())
    time.sleep(1)

print("Simulation completed")
simulator.exit()
