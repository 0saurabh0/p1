from satsim import Service, InvalidEventTime, InvalidCycleTme


class Scheduler(Service):

    def __init__(self, simulator):
        self._simulator = simulator
        self._scheduled_events = {}
        self._immediate_events = {}

    def add_simulation_time_event(
            self, entry_point, simulation_time, cycle_time=0, repeat=0):
        # if simulation_time.total_seconds() < 0: (before)
        if simulation_time < 0:
            raise InvalidEventTime()

        elif repeat != 0 and cycle_time <= 0:
            raise InvalidCycleTme()

        else:
            event_id = self._simulator.get_event_manager().create_new_event()
            self._scheduled_events[event_id] = {
                'entry_point': entry_point,
                'simulation_time': simulation_time,
                'cycle_time': cycle_time,
                'repeat': repeat}
            return event_id

    # def add_mission_time_event(
    #         self, entry_point, mission_time, cycle_time=0, repeat=0):
    #     if mission_time < self.current_mission_time:
    #         raise InvalidEventTime()
    #     if repeat != 0 and cycle_time <= 0:
    #         raise InvalidCycleTme()
    #     else:
    #         # add sim time to event
    #         return self.event_id

    # def add_epoch_time_event(
    #         self, entry_point, epoch_time, cycle_time=0, repeat=0):
    #     if epoch_time < self.current_epoch_time:
    #         raise InvalidEventTime()
    #     if (repeat != 0 and cycle_time <= 0):
    #         raise InvalidCycleTime()
    #     else:
    #         # add sim time to event
    #         return self.event_id

    # def add_zulu_time_event(
    #         self, entry_point, zulu_time, cycle_time=0, repeat=0):
    #     if zulu_time < self.current_zulu_time:
    #         raise InvalidEventTime()
    #     if (repeat != 0 and cycle_time <= 0):
    #         raise InvalidCycleTime()
    #     else:
    #         # add sim time to event
    #         return self.event_id

    def add_immediate_event(self, entry_point):
        event_id = self._simulator.get_time_keeper().create_new_event()
        self._immediate_events[event_id] = {'entry_point': entry_point}
        return event_id

    def remove_event(self, event_id):
        if event_id not in self._scheduled_events:
            raise InvalidEventId()

        elif False:  # TODO: set repeat to 0 for an executing event
            pass   # TODO elfi

        else:
            del self._scheduled_events[event_id]

    def set_event_simulation_time(self, event_id, simulation_time):
        raise NotImplementedError
        # if simulation_time < 0:
        #     # the Event is never executed but instead removed immediately from the
        #     # scheduler
        #     remove_event(event_id)
        #     # if event_id '''not currently on the scheduler''':
        #     #     raise InvalidEventId()
        #     #
        #     # if event_id '''not scheduled on simulation time''':
        #     #     raise InvalidEventId()
        #
        # if event_id '''not currently on the scheduler''' or event_id '''not scheduled on simulation time''':
        #     raise InvalidEventId()
        # else:
        #     # update the simulation time of event
        #     pass

    def set_event_mission_time(self, event_id, mission_time):
        raise NotImplementedError
        # if event_id '''not in the scheduler''' :
        #     raise InvalidEventId()

        # if event_id '''not scheduled on mission time''':
        #     raise InvalidEventId()

        # if event_id '''not in the scheduler''' or event_id '''not scheduled on mission time''':
        #     raise InvalidEventId()
        #
        # if mission_time < self.current_mission_time:
        #     remove_event(event_id)
        #
        # else:
        #     # update mission time of event
        #     pass

    def set_event_epoch_time(self, event_id, epoch_time):
        raise NotImplementedError
        # """.
        # shall update the Epoch time of the next execution of an Event
        # """
        # # if event_id '''not in the scheduler''' :
        # #     raise InvalidEventId()
        # #
        # # if event_id '''not scheduled on epoch time''':
        # #     raise InvalidEventId()
        #
        # if event_id '''not in the scheduler''' or event_id '''not scheduled on epoch time''':
        #     raise InvalidEventId()
        #
        # if epoch_time < self.current_epoch_time:
        #     remove_event(event_id)
        #
        # else:
        #     # update epoch time of event
        #     pass

    def set_event_zulu_time(self, event_id, zulu_time):
        raise NotImplementedError
        # """.
        # shall update the Zulu time of the next execution of an Event
        # """
        # # if event_id '''not in the scheduler''' :
        # #     raise InvalidEventId()
        # #
        # # if event_id '''not scheduled on zulu time''':
        # #     raise InvalidEventId()
        #
        # if event_id '''not in the scheduler''' or event_id '''not scheduled on zulu time''':
        #     raise InvalidEventId()
        #
        # if zulu_time < self.current_zulu_time:
        #     remove_event(event_id)
        #
        # else:
        #     # update zulu time of event
        #     pass

    def set_event_cycle_time(self, event_id, cycle_time):
        raise NotImplementedError

        # if event_id '''not in the scheduler''':
        #     raise InvalidEventId()
        #
        # # repeat undefinied in the function
        # if (repeat != 0 and cycle_time <= 0):
        #     raise InvalidCycleTme()
        #
        # else:
        #     # update the cycle_time of the event
        #     pass

    def set_event_count(self, event_id, count):
        raise NotImplementedError
        # if event_id '''not in the scheduler''':
        #     raise InvalidEventId()
        #
        # if (count != 0 and self.cycle_time == 0):
        #     raise InvalidCycleTme()
        #
        # if (count > 0 and event_id == self.event_id):
        #     # the scheduler executes the Event for the given Count, excluding the
        #     # current execution
        #     pass
        #
        # if count == 0:
        #     # the Event is removed immediately after its execution is finished
        #     # execute
        #     remove_event(event_id)
        #
        #     pass

    def get_current_event_id(self):
        raise NotImplementedError
        # # try :
        # #     if '''an event is currently executing''':
        # #         return self.event_id
        # # except:
        # #     return -1
        #
        # if '''an event is currently executing''':
        #     return self.event_id
        # else:
        #     return -1

    def get_next_scheduled_event_time(self):
        raise NotImplementedError
        # """.
        # return the Simulation Time of the execution of the
        # next scheduled Simulation Time, Epoch Time or Mission Time Event
        # """
        # # event scheduled in zulu time are not considered
        # #
        # pass
