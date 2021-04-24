from satsim import Service, InvalidEventName, EntryPointAlreadySubscribed,\
    InvalidEventId


class EventManager(Service):

    def __init__(self):
        self._event_list = []
        self.EVENT = {
            1: "LEAVE_CONNECTING",
            2: "ENTER_INITIALISING",
        }
        # LEAVE_INITIALISING=3,
        # ENTER_STANDBY=4,
        # LEAVE_STANDBY=5,
        # ENTER_EXECUTING=6,
        # LEAVE_EXECUTING=7,
        # ENTER_STORING=8,
        # LEAVE_STORING=9,
        # ENTER_RESTORING=10,
        # LEAVE_RESTORING=11,
        # ENTER_EXITING=12,
        # ENTER_ABORTING=13,
        # EPOCH_TIME_CHANGED=14,
        # MISSION_TIME_CHANGED=15,
        # ENTER_RECONNECTING=16,
        # LEAVE_RECONNECTING=17,
        # PRE_SIM_TIME_CHANGE=18,
        # POST_SIM_TIME_CHANGE=19)

    def query_event_id(self, event_name):
        if not event_name.strip():
            raise InvalidEventName()

        for key, value in self.EVENT.items():
            if event_name == key:
                return value
        else:
            return None

    def subscribe(self, event_id, entry_point):
        if (event_id, entry_point) in self._event_list:
            raise EntryPointAlreadySubscribed()

        if event_id not in self.EVENT:
            raise InvalidEventId()

        self._event_list.append((event_id, entry_point))

    def unsubscribe(self, event_id, entry_point):
        if (event_id, entry_point) in self._event_list:
            raise EntryPointAlreadySubscribed()

        if event_id not in self.EVENT:
            raise InvalidEventId()

        self._event_list.remove((event_id, entry_point))

    def emit(self, event_id, synchronous):
        # TODO: allow for asynchronous, non-blocking, call
        for _event_id, entry_point in self._event_list:
            if _event_id == event_id:
                entry_point()
