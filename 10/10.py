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

grid = read_grid_2d("10")



start_time = time.time()




print("PART 1:")

graph = grid_to_graph(grid)
def p1(graph, start_node, values=[]):
    count = 0
    queue = []
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if values and node.value not in values:
            continue
        for n in node.adjacency_list:
            if int(n.value) == int(node.value) + 1:
                if n.value == '9' and not n.visited:
                    count += 1
                n.visited = True
                queue.append(n)
    graph.reset()
    return count


print(sum(p1(graph, n) for n in graph.nodes if n.value == "0"))

def p2(graph, start_node):
    count = 0
    queue = []
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        for n in node.adjacency_list:
            if int(n.value) == int(node.value) + 1:
                if n.value == '9' and not n.visited:
                    count += 1
                    
                queue.append(n)

    return count

print(sum(p2(graph, n) for n in graph.nodes if n.value == "0"))





print("PART 2:")





print()

print("took %s seconds" % (time.time() - start_time))