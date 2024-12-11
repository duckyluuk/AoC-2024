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

nums = to_nums(read_raw_text("11").split())



start_time = time.time()


def calc(stone):
    str_stone = str(stone)
    if stone == 0:
        return [1]
    elif len(str_stone) % 2:
        return [stone * 2024]
    else:
        half = len(str_stone) // 2
        return [int(str_stone[:half]), int(str_stone[half:])]



print("PART 1:")
stones = [*nums]
for i in range(25):
    new = []
    for stone in stones:
        new += calc(stone)
    stones = new

print(len(stones))


print("PART 2:")
stones = {}
for n in nums:
    stones[n] = stones.get(n, 0) + 1

for i in range(75):
    new = {}
    for stone, cnt in stones.items():
        for res in calc(stone):
            new[res] = new.get(res, 0) + cnt
    stones = new

print(sum(cnt for stone, cnt in stones.items()))


print("took %s seconds" % (time.time() - start_time))