from .object import Object


class EntryPointPublisher(Object):

    """An entry point publisher is a component that publishes entry points.

    The entry points may be registered, for example, with the Scheduler or
    the Event Manager services. This is an optional interface. It needs to be
    implemented by components which want to provide access to their entry
    points by name.
    """

    def __init__(self):
        pass

    def get_entry_points(self):
        """Query for the collection of all entry points of the component.

        Returns
        -------
        list
            a list of entry points. Empty if no entry points exist.
        """

        pass

    def get_entry_point(self, name):
        """Query for an entry point of this component by its name.

        Parameters
        ----------
        name : str
            Entry point name

        Returns
        -------
        list
            a list of entry points. Null if entry point could not be found.
        """

        pass
