# allow importing from parent folder
import sys
sys.path.append('../AOC-2024')

# util imports
from utils.readfile import *
from utils.calc import *
from utils.graph import *
from utils.util import *
# lib imports
import re
import math
import copy
import numpy as np
from itertools import combinations, permutations, product
import re
import time

# input parsing
lns = to_nums([x.split() for x in read_lines_list("1")])

print(*zip(*lns))

start_time = time.time()


print("PART 1:")
lines = [*lns]
pairs = list(zip(*list(map(sorted,list(zip(*lines))))))

print(sum(abs(a-b) for a,b in pairs))



print("PART 2:")
lines = [*lns]
a, b = list(zip(*lines))


print(sum(b.count(x) * x for x in a))



print("took %s seconds" % (time.time() - start_time))