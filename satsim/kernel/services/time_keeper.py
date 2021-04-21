from satsim import Service

class TimeKeeper(Service):

    EVENT_ID

    def __init__(self):
        # public or private attributes ??

        self.epoch_time = ""
        self.mission_start_time = ""
        self.mission_time = ""
        self.simulation_time = ""
        self.zulu_time = ""


    def set_epoch_time(self, epoch_time):
        self.epoch_time = epoch_time
        # emit SMP Epoch time changed global SMP event
        # EpochTimeChanged_EventId = 14



    def get_epoch_time(self):
        return self.epoch_time


    def set_mission_start_time(self, ):


    def get_mission_start_time(self):
        return self.mission_start_time


    def set_mission_time(self, ):


    def get_mission_time(self):
        return self.mission_time


    def set_simulation_time(self, ):


    def get_simulation_time(self):
        return self.simulation_time


    def get_zulu_time(self):
        return self.zulu_time
