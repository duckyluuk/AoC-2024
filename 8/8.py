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

grid = read_grid_2d("8")



start_time = time.time()

points = {

}

for y in range(50):
    for x in range(50):
        if grid[y][x] != ".":
            points[grid[y][x]] = points.get(grid[y][x], []) + [(x, y)]

print(points)


print("PART 1:")

n = 0

uniq = set()

for key in points:
    curpoints = points[key]
    for p1 in curpoints:
        for p2 in curpoints:
            xdis = p2[0] - p1[0]
            ydis = p2[1] - p1[1]

            if p1 != p2:
                uniq |= {(p1[0] - xdis, p1[1] - ydis)}






print(len([(x, y) for x, y in uniq if x >= 0 and y >= 0 and x < 50 and y < 50]))



print("PART 2:")

uniq = set()

for key in points:
    curpoints = points[key]
    for p1 in curpoints:
        for p2 in curpoints:
            xdis = p2[0] - p1[0]
            ydis = p2[1] - p1[1]

            x = p1[0]
            y = p1[1]
            for _ in range(50):
                uniq |= {(x, y)}
                x -= xdis
                y -= ydis







print(len([(x, y) for x, y in uniq if x >= 0 and y >= 0 and x < 50 and y < 50]))



print("took %s seconds" % (time.time() - start_time))