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

grid = read_grid_2d("12")

positions = {(x, y): cell for y, row in enumerate(grid) for x, cell in enumerate(row)}


start_time = time.time()



print("PART 1:")
total = 0
visited = set()
for ((x, y), cell) in positions.items():
    if (x, y) in visited:
        continue
    queue = [(x, y)]
    area = 0
    border = 0
    while queue:
        (x, y) = queue.pop(0)
        if (x, y) in visited:
            continue
        area += 1
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if positions.get((x+dx, y+dy)) == cell:
                queue.append((x+dx, y+dy))
            else:
                border += 1

    total += area * border
print(total)


print("PART 2:")
total = 0
visited = set()
for ((x, y), cell) in positions.items():
    if (x, y) in visited:
        continue
    queue = [(x, y)]
    corners = 0
    area = 0
    while queue:
        (x, y) = queue.pop(0)
        if (x, y) in visited:
            continue

        area += 1
        visited.add((x, y))
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(4):
            (dx1, dy1), (dx2, dy2), *_ = directions
            if positions.get((x+dx1, y+dy1)) != cell and positions.get((x+dx2, y+dy2)) != cell:
                corners += 1
            elif positions.get((x+dx1, y+dy1)) == cell and positions.get((x+dx2, y+dy2)) == cell:
                if positions.get((x+dx1 + dx2, y+dy1 + dy2)) != cell:
                    corners += 1
            directions = directions[1:] + directions[:1]

        for dx, dy in directions:
            if positions.get((x+dx, y+dy)) == cell:
                queue.append((x+dx, y+dy))


    total += area * corners
print(total)


print("took %s seconds" % (time.time() - start_time))