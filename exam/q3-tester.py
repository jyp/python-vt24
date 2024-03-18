from outcheck import *
from q3 import *
import math

k = Kepler()

k.observe("earth", 0, 0)
k.observe("earth", 2*math.pi, 31548499)
k.observe("x1", 0, 0)
k.observe("x1", 1, 100)
k.observe("x1", 2, 150)


report("get_period",
       check_eq(k.get_period("x1"),471.23889803846896))

report("get_radius",
       check_eq(k.get_radius("x1"),90734658.06262995))

report("print_planets",
       check_output(k.print_planets,
                    ["earth 31548499.0 149599997641.41833",
                     "x1 471.23889803846896 90734658.06262995"]))

k.print_planets()
