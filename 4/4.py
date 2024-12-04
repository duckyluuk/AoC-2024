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


grid = read_raw_text("4")
width = grid.index("\n")+1

start_time = time.time()


print("PART 1:")

n = 0
for i in range(len(grid)):
    if grid[i]=="X":
        for x in [1,-1,width,-width,width-1,width+1,-width+1,-width-1]:
            n += grid[i::x][:4] == "XMAS"

print(n)



print("PART 2:")

n = 0
for i in range(width, len(grid) - width - 1):
    if grid[i]=="A":
        l = grid[i-width-1] + grid[i+width+1] 
        m = grid[i-width+1] + grid[i+width-1]
        n += (m in ["MS", "SM"]) and l in ["MS", "SM"]

print(n)