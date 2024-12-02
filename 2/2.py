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


lns = to_nums([x.split() for x in read_lines_list("2")])

print(*zip(*lns))

start_time = time.time()


print("PART 1:")
lines = [*lns]
safe = 0
for line in lines:
    if all(0 < a-b < 4 for a,b in zip(line, line[1:])) or all(0 < a-b < 4 for a,b in zip(line[::-1], line[::-1][1:])):
        safe+=1



print(safe)



print("PART 2:")
lines = [*lns]
safe = 0
for ln in lines:
    for i in range(len(ln)+1):
        line = [*ln]
        line = line[:i]+line[i+1:]
        if all(0 < a-b < 4 for a,b in zip(line, line[1:])) or all(0 < a-b < 4 for a,b in zip(line[::-1], line[::-1][1:])):
            safe+=1
            break



print(safe)



print("took %s seconds" % (time.time() - start_time))