import time
start = time.time()

positions = {pos: cell for pos, cell in enumerate(open(0).read()) if cell != "\n"}

t1 = 0
t2 = 0
visited = set()
for (pos, cell) in positions.items():
    queue = [pos]
    corners = 0
    area = 0
    sides = 0
    while queue:
        pos = queue.pop(0)
        if pos in visited:
            continue

        area += 1
        visited.add(pos)
        directions = [141, 1, -141, -1]
        for i in range(4):
            d1, d2, *_ = directions
            if positions.get(pos+d1) != cell and positions.get(pos+d2) != cell:
                corners += 1
            elif positions.get(pos+d1) == cell and positions.get(pos+d2) == cell:
                if positions.get(pos+d1+d2) != cell:
                    corners += 1
            directions = directions[1:] + directions[:1]

        for d in directions:
            if positions.get(pos+d) == cell:
                queue.append(pos+d)
            else: 
                sides += 1

    t1 += area * sides
    t2 += area * corners
print(t1, t2)

print(time.time() - start)