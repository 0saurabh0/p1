from satsim import Component

# models can be fallible by implementing the fallible model interface
# models are added to the sim via the simulator add_model
# models can be dynamically added after first startup of the simulator in the building
# phase, also in stand-by-started


class Model(Component):
    pass
