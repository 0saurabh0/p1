from satsim import Service, InvalidEventTime, InvalidCycleTme


class Scheduler(Service):


    def __init__(self):
        self.event_id = ""
        self.current_mission_time = " "
        self.current_epoch_time
        self.current_zulu_time


    def add_simulation_time_event(self, entry_point, simulation_time, cycle_time, repeat):
        if (simulation_time < 0) :
            raise InvalidEventTime()
            # the Event is not added to the scheduler and never executed
        # do we need elif instead of if (would break at first error)
        if (repeat != 0 and cycle_time <= 0):
            raise InvalidCycleTme()
            # the Event is not added to the scheduler and never executed
        else:
            # add sim time to event
            return self.event_id


    def add_mission_time_event(self, entry_point, mission_time, cycle_time, repeat):
        if mission_time < self.current_mission_time :
            raise InvalidEventTime()
        if (repeat != 0 and cycle_time <= 0):
            raise InvalidCycleTme()
        else:
            # add sim time to event
            return self.event_id


    def add_epoch_time_event(self, entry_point, epoch_time, cycle_time, repeat):
        if epoch_time < self.current_epoch_time :
            raise InvalidEventTime()
        if (repeat != 0 and cycle_time <= 0):
            raise InvalidCycleTime()
        else:
            # add sim time to event
            return self.event_id


    def add_zulu_time_event(self, entry_point, zulu_time, cycle_time, repeat):
        if zulu_time < self.current_zulu_time :
            raise InvalidEventTime()
        if (repeat != 0 and cycle_time <= 0):
            raise InvalidCycleTime()
        else:
            # add sim time to event
            return self.event_id


    def add_immediate_event(self, entry_point):
        ''' The scheduled event is inserted at the front of the list of events
        scheduled for the current simulation time making it the next event to
        be executed'''
        # add event
        # repeat, cycle_time, simulation_time = 0

        return self.event_id


    def remove_event (self, event_id):
        # for event in event_scheduled
        if event_id not...

        if event_id == self.event_id :
            # equivalent to set the repeat=0 via the set_event_count



    def set_event_simulation_time(self, event_id, simulation_time):
        pass


    def set_event_mission_time(self, event_id, mission_time):
        pass


    def set_event_epoch_time(self, event_id, epoch_time):
        pass


    def set_event_zulu_time(self, event_id, zulu_time):
        pass


    def set_event_cycle_time(self, event_id, cycle_time):
        pass


    def set_event_count(self, event_id, count):
        pass


    def get_current_event_id(self, event_id):
        if #event executing
            return event_id
        else :
            return -1
