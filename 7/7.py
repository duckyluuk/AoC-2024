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

lines = read_lines_list("7")



start_time = time.time()




print("PART 1:")

n = 0

for line in lines:
    res, *vals = line.split(" ")
    res = int(res[:-1])
    results, *vals = to_nums(vals)
    results = [results]
    while vals:
        num, *vals = vals
        new = []
        for op in int.__add__, int.__mul__:
            for v in results:
                if v<res:new.append(op(v, num))
        results = new
    
    n += res in results and res

print(n)



print("PART 2:")

n = 0

for line in lines:
    res, *vals = line.split(" ")
    res = int(res[:-1])
    results, *vals = to_nums(vals)
    results = [results]
    while vals:
        num, *vals = vals
        new = []
        for op in int.__add__, int.__mul__, lambda a, b: int(str(a) + str(b)):
            for v in results:
                if v<res:new.append(op(v, num))
        results = new
    
    n += res in results and res

print(n)


print("took %s seconds" % (time.time() - start_time))