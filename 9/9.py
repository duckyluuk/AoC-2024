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

num = read_raw_text("9")



start_time = time.time()




print("PART 1:")


isfile = True
nums = []
id = 0
for x in num:
    if isfile:
        nums += [id]*int(x)
        id = id+1
    else:
        nums += ["."]*int(x)
    isfile = not isfile


i = 0
while i < len(nums):
    while nums[-1] == ".":
        nums = nums[:-1]
    if nums[i] == ".":
        nums[i] = nums.pop(-1)
    i = i+1

print(sum(i*x for i,x in enumerate(nums)))





print("PART 2:")

values = []
space = []
final = []

pos = 0
id = 0
is_file = True
for i, size in enumerate(num):
    size = int(size)
    if is_file:
        values += [(pos, size, id)]
        final += [id] * size
        id += 1
    else:
        space += [(pos, size)]
        final += [0] * size
    is_file = not is_file
    pos += size


for pos, size, id in values[::-1]:
    for space_idx, (space_pos, space_size) in enumerate(space):
        if space_pos < pos and size <= space_size:
            final[pos:pos+size] = [0] * size
            final[space_pos:space_pos+size] = [id] * size
            space[space_idx] = (space_pos + size, space_size - size)
            break


print(sum(i*c for i,c in enumerate(final)))

print("took %s seconds" % (time.time() - start_time))