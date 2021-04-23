from satsim import Service, InvalidEventName, EntryPointAlreadySubscribed
from satsim import EntryPointNotSubscribed, InvalidEventId


class EventManager(Service):

    SMP_EVENTS = dict(LEAVE_CONNECTING=1,
                      ENTER_INITIALISING=2,
                      LEAVE_INITIALISING=3,
                      ENTER_STANDBY=4,
                      LEAVE_STANDBY=5,
                      ENTER_EXECUTING=6,
                      LEAVE_EXECUTING=7,
                      ENTER_STORING=8,
                      LEAVE_STORING=9,
                      ENTER_RESTORING=10,
                      LEAVE_RESTORING=11,
                      ENTER_EXITING=12,
                      ENTER_ABORTING=13,
                      EPOCH_TIME_CHANGED=14,
                      MISSION_TIME_CHANGED=15,
                      ENTER_RECONNECTING=16,
                      LEAVE_RECONNECTING=17,
                      PRE_SIM_TIME_CHANGE=18,
                      POST_SIM_TIME_CHANGE=19)


def __init__(self):
    pass


def query_event_id(self, event_name):
    """.

    returns the event identifier for an events
    · If called with the name of one of the pre-defined Event types -->
    returns the corresponding EventId.
    · If called with a non-empty event name different from all
    pre-defined event types --> returns an event identifier different
    from all pre-defined event identifiers.
    · If called with the same name again in the context of a restored
    simulation, it returns always the same event identifier.
    """
    if not event_name.strip():
        raise InvalidEventName()

        for key, value in SMP_EVENTS.items():
            if event_name == key:
                return value


def event_manager_subscribe(self, event, entry_point):
    """.

    If called with a pair of event identifier and entry point that is not
    currently in the internal list, it adds this pair to the internal list
    """
    if '''event and entrypoint in the list ''':
        raise EntryPointAlreadySubscribed()

    if '''event don't exist''':
        raise InvalidEventId()


def event_manager_unsubscribe(self, event, entry_point):
    """.

    If called with a pair of event identifier and entry point that is
    currently in the internal list, it removes this
    pair to the internal list
    """
    if '''event and entrypoint in not the list ''':
        raise EntryPointNotSubscribed()

    if '''invalid event id''':
        raise InvalidEventId()


def event_manager_emit(self, event_id, synchronous):
    pass
