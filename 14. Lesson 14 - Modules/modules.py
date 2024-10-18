import math
import sys
import random

# 2. you can import specific items required from modules
from enum import Enum
from math import pi

# Creating an alias
import random as rdm


print(math.pi) # 1
print("")

print(pi) # 2
print("")

print(random.choice("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print("")

print(rdm.choice("asdasfasdfadfsgs"))
print("")

# how to know what is inside of a module
# dir function
print(dir(rdm))

# put one of each on each line
for item in dir(rdm):
    print(item)

print("")
print("")
# YOu can also use the dot notation

# WORKING WITH MODULES
import kansas
print(kansas.capital)
kansas.randomfunfact();

from rps_scope_update_7 import rock_paper_scissors
print(__name__)
print(kansas.__name__)
rock_paper_scissors()