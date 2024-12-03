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


lns = read_raw_text("3")

start_time = time.time()


print("PART 1:")
lines = lns

res = 0
for x in re.findall(r"mul\(\d+,\d+\)",lines):
    x=x[4:-1].split(",")
    res += int(x[0]) * int(x[1])




print(res)



print("PART 2:")
lines = lns

res = 0
enabled = True
for x in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)",lines):
    if x=="do()":enabled=True
    if x=="don't()":enabled=False
    if enabled and x.startswith("mul"):
        x=x[4:-1].split(",")
        res += int(x[0]) * int(x[1])




print(res)



print("took %s seconds" % (time.time() - start_time))