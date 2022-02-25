import argparse
import importlib

import satsim

# load model from external file
parser = argparse.ArgumentParser()
parser.add_argument('modelfile')
args = parser.parse_args()
model = importlib.import_module(args.modelfile)

# create simulator
simulator = satsim.Simulator()
simulator.set_time_progress(satsim.SimulationTimeProgress.REALTIME)
# simulator.set_time_progress(satsim.SimulationTimeProgress.ACCELERATED, 10)
# simulator.set_time_progress(satsim.SimulationTimeProgress.FREE_RUNNING)

# add models
simulator.add_model(model.root)

# simulator setup
simulator.publish()
simulator.configure()
simulator.connect()

# start executing simulation
print("Simulation running...")
print("Press <Enter> to stop")
print()
simulator.run()
input()
model.root.get_hot_object("HO_1").set_status(False)
input()

print("Simulation completed")
simulator.hold()
simulator.exit()
