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


root = Counter("Counter", "A simple counter", None)
