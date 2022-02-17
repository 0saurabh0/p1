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
simulator.initialise()

# start executing simulation
simulator.run()
print("Simulation running...")

# run for some time
input("Press <Enter> to stop\n")

print("Simulation completed")
simulator.hold()
simulator.exit()
