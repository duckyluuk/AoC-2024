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


rules, updates = read_groups("5")

rules = [list(map(int,x.split("|"))) for x in rules]
updates = [list(map(int,x.split(","))) for x in updates]

start_time = time.time()




print("PART 1:")

n = 0

for update in updates:
    success = True
    for rule in rules:
        try:
            a, b = update.index(rule[0]), update.index(rule[1])
            if a > b:
                success = False
        except:
            continue
    if success:
        n += update[len(update)//2]

print(n)



print("PART 2:")

n = 0

for update in updates:
    success = True
    i = 0
    while i < len(rules):
        rule = rules[i]
        i += 1
        try:
            a, b = update.index(rule[0]), update.index(rule[1])
            if a > b:
                success = False
                update[a], update[b] = update[b], update[a]
                i = 0
        except:
            continue

    if not success:
        n += update[len(update)//2]



print(n)


print("took %s seconds" % (time.time() - start_time))