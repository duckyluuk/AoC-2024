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


grid = read_raw_text("6")
width = grid.index("\n")+1


start_time = time.time()




print("PART 1:")

uniq = set()
pos = grid.index("^")
dirs = [-width, 1, width, -1]
dir = 0

fail = 0
while grid[pos] != "\n" and fail == 0:
    try: 
        uniq |= {pos}
        if grid[pos+dirs[dir]] == "#":
            dir = (dir+1)%4
        else:
            pos += dirs[dir]
    except: fail = 1




print(len(uniq))



print("PART 2:")

n = 0

for check in uniq:
    seen = set()
    pos = grid.index("^")
    dir = 0

    while 1:
        if (pos, dir) in seen:
            n += 1
            break
        if not (0 <= pos < len(grid)) or grid[pos] == "\n":
            break
        if grid[pos] == "#" or pos==check:
            pos -= dirs[dir]
            dir = (dir+1)%4
        else:
            seen |= {(pos, dir)}
            pos += dirs[dir]



print(n)


print("took %s seconds" % (time.time() - start_time))