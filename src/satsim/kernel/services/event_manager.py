from ..service import Service


class EntryPointAlreadySubscribed(Exception):
    pass


class InvalidEventId(Exception):
    pass


PREDEFINED_EVENTS = {
    1: "LEAVE_CONNECTING",
    2: "ENTER_INITIALISING",
    3: "LEAVE_INITIALISING",
    4: "ENTER_STANDBY",
    5: "LEAVE_STANDBY",
    6: "ENTER_EXECUTING",
    7: "LEAVE_EXECUTING",
    8: "ENTER_STORING",
    9: "LEAVE_STORING",
    10: "ENTER_RESTORING",
    11: "LEAVE_RESTORING",
    12: "ENTER_EXITING",
    13: "ENTER_ABORTING",
    14: "EPOCH_TIME_CHANGED",
    15: "MISSION_TIME_CHANGED",
    16: "ENTER_RECONNECTING",
    17: "LEAVE_RECONNECTING",
    18: "PRE_SIM_TIME_CHANGE",
    19: "POST_SIM_TIME_CHANGE"
}


class EventManager(Service):

    def __init__(self, simulator):
        self._simulator = simulator

        self._event_entrypoint_pairs = []
        self._events = PREDEFINED_EVENTS
        self._event_count = len(self._events)

    def query_event_id(self, event_name):
        for id, name in self._events.items():
            if event_name == name:
                return id
        return None

    def subscribe(self, event_id, entry_point):
        if (event_id, entry_point) in self._event_entrypoint_pairs:
            raise EntryPointAlreadySubscribed()

        if event_id not in self._events:
            raise InvalidEventId()

        self._event_entrypoint_pairs.append((event_id, entry_point))

    def unsubscribe(self, event_id, entry_point):
        if (event_id, entry_point) in self._event_entrypoint_pairs:
            raise EntryPointAlreadySubscribed()

        if event_id not in self._events:
            raise InvalidEventId()

        self._event_entrypoint_pairs.remove((event_id, entry_point))

    def emit(self, event_id, synchronous=True):
        # TODO: allow for asynchronous, non-blocking, call
        for _event_id, entry_point in self._event_entrypoint_pairs:
            if _event_id == event_id:
                entry_point()

    def create_new_event(self, name=None):
        self._event_count += 1
        self._events[self._event_count] = name
        return self._event_count
