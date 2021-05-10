from satsim import Service


class Resolver(Service):

    def __init__(self):
        pass

    def resolve_absolute(self, absolute_path):
        """returns a reference to a component, field, failure container, reference,
        event sink, event source or entry point Object in the simulation.
        argument:
        absolute_path: giving the absolute path string of the Object
        behaviour:
        If the absolute_path does not give the path to an object, it returns nullptr;
        If no object with the given path can be found, it returns nullptr;
        If absolute_path resolves to an object, it returns the Object reference to the object."""

        raise NotImplementedError

    def resolve_relative(self, relative_path):
        raise NotImplementedError
