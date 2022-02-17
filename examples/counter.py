import satsim


class Counter(satsim.Model):

    def configure(self):
        self._count = 0
        self.count_entrypoint =\
            satsim.EntryPoint("Increase Counter", function=self.count)
        self.reset_entrypoint =\
            satsim.EntryPoint("Reset Counter", function=self.reset)

    def connect(self):
        self.scheduler.add_simulation_time_event(
            self.count_entrypoint, simulation_time=1, cycle_time=1, repeat=-1)
        self.scheduler.add_simulation_time_event(self.reset_entrypoint, 4)
        self.logger.log_debug(self, "Counter Model is now connected")

    def reset(self):
        self._count = 0

    def count(self):
        self._count += 1
        self.logger.log_debug(self, f"count is now {self._count}")

    def add(self, offset):
        self._count += offset
        return self._count


counter = Counter("Counter", "A simple counter", None)

##############################################################################

# create simulator
simulator = satsim.Simulator()
simulator.set_time_progress(satsim.SimulationTimeProgress.REALTIME)
# simulator.set_time_progress(satsim.SimulationTimeProgress.ACCELERATED, 10)
# simulator.set_time_progress(satsim.SimulationTimeProgress.FREE_RUNNING)

# add models
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
input("Press <Enter> to stop\n")

print("Simulation completed")
simulator.hold()
simulator.exit()
