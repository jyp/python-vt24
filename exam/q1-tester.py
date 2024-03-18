# test:
# seconds_per_day = 24*60*60
# print(kepler(radii["earth"]))

from outcheck import *
from q1 import *


report("earth",
       check_output(lambda: planet_period("earth"),
                    ["31548499.746086624"]))
report("whatever",
       check_output(lambda: planet_period("whatever"),
                    ["Unknown planet"]))

