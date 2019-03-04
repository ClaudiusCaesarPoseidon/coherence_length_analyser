import os
#from ...lib import functions

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#max_back = -2500
#max_for = 2500

#path = functions.resource_path(os.path.join("data", "motor_extrema.txt"))
path = os.path.join(__location__, "motor_extrema.txt")
# loads the extremas for the motor from file or creates it with default values
try:
    with open(path, "r") as file:
        tmp = file.read().split("\n")
        max_back = int(tmp[0].split("=")[-1])
        max_for = int(tmp[1].split("=")[-1])
except FileNotFoundError:
    with open(path, "w") as file:
        file.write("max_back = -2500\nmax_for = 2500")
        max_back = -2500
        max_for = 2500
