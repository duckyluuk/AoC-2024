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


nums = force_nums(read_lines_list("14"))


start_time = time.time()



print("PART 1:")
total = 0

seconds = 100
width = 101
height = 103
positions = []
for x,y,vx,vy in nums:
    positions.append([(x+vx*seconds)%width, (y+vy*seconds)%height])


q1 = sum(1 for x,y in positions if x<50 and y<51)
q2 = sum(1 for x,y in positions if x>50 and y<51)
q3 = sum(1 for x,y in positions if x<50 and y>51)
q4 = sum(1 for x,y in positions if x>50 and y>51)

print(q1 * q2 * q3 * q4)


print("PART 2:")
total = 0

print(total)
positions = [*nums]
for i in range(999999):
    if sum(1 for x,y,vx,vy in positions if x>45 and x<55 and y>46 and y<56)>25:
        print(sum(1 for x,y,vx,vy in positions if x>45 and x<55 and y>46 and y<56))
        uniqpos = {(x,y) for  x,y,vx,vy in positions}
        grid = "\n".join("".join(".#"[(x,y) in uniqpos]for x in range(101))for y in range(103))
        print(grid)
        print(i)
        input()
    positions = [
        ((x + vx) % width, (y + vy) % height, vx, vy)
          for x, y, vx, vy in positions
    ]




print("took %s seconds" % (time.time() - start_time))

