# allow importing from parent folder
import sys
sys.path.append('../AOC-2024')

from utils.readfile import *
from utils.calc import *
from utils.graph import *
from utils.util import *
import re
import math
import copy
import numpy as np
from itertools import combinations, permutations, product
import re
import time
import z3

groups = force_nums(read_groups("13"))


start_time = time.time()



print("PART 1:")
total = 0

for group in groups:
    [ax, ay], [bx, by], [px, py] = group
    s = z3.Solver()
    da, db = z3.Ints("da db")
    s.add(ax * da + bx * db == px)
    s.add(ay * da + by * db == py)

    if s.check() == z3.sat:
        total += s.model()[da].as_long() * 3 + s.model()[db].as_long()

print(total)


print("PART 2:")
for group in groups:
    [ax, ay], [bx, by], [px, py] = group
    px, py = px+10000000000000, py+10000000000000
    s = z3.Solver()
    da, db = z3.Ints("da db")
    s.add(ax * da + bx * db == px)
    s.add(ay * da + by * db == py)

    if s.check() == z3.sat:
        total += s.model()[da].as_long() * 3 + s.model()[db].as_long()

print(total)




print("took %s seconds" % (time.time() - start_time))

