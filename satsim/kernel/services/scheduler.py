from satsim import Service


class Scheduler(Service):
    def __init__(self):
        pass

    def remove_event(self):
        pass


    def add_simulation_time_event(self, entry_point, simulation_time, cycle_time, repeat):
        if (simulation_time < 0):
            # it throws an InvalidEventTime exception --> the Event is not added to the scheduler and never executed
            pass
        if (repeat != 0 and cycle_time <= 0):
            # it throws an InvalidCycleTme exception --> the Event is not added to the scheduler and never executed
            pass

        return event_id #not defined ??


    def add_mission_time_event(self, entry_point, mission_time, cycle_time, repeat):
        #If the Mission Time < the current mission time, it throws an InvalidEventTime exception --> the Event is not added to the scheduler and never executed;
        if (repeat != 0 and cycle_time <= 0):
            #it throws an InvalidCycleTime exception
            pass
        return event_id


    def add_epoch_time_event(self, entry_point, epoch_time, cycle_time, repeat):
        #If the Epoch Time is less than the current epoch time it throws an InvalidEventTime exception
        if (repeat != 0 and cycle_time <= 0):
            #it throws an InvalidCycleTime exception
            pass
        return event_id

    def add_zulu_time_event(self, entry_point, zulu_time, cycle_time, repeat):
        #If the given Zulu Time is less than the current Zulu time, it throws an InvalidEventTime exception
        if (repeat != 0 and cycle_time <= 0):
            #it throws an InvalidCycleTime exception
            pass
        return event_id

    def add_immediate_event(self, entry_point):
        ''' The scheduled event is inserted at the front of the list of events scheduled for
        the current simulation time making it the next event to be executed;'''
        return event_id

    def remove_event (self, event_id):
        pass

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

    def get_current_event_id (self, event_id):
        if #event executing
            return event_id
        else :
            return -1
