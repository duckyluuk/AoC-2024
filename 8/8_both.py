import time

grid = *open(0),



start_time = time.time()

points = {}

for y in range(50):
    for x in range(50):
        if grid[y][x] != ".":
            points[grid[y][x]] = points.get(grid[y][x], []) + [(x, y)]



uniq = set()
for test2 in 0, 1:
    for key in points:
        curpoints = points[key]
        for p1 in curpoints:
            for p2 in curpoints:
                xdis = p2[0] - p1[0]
                ydis = p2[1] - p1[1]

                x = p1[0]
                y = p1[1]

                if p1 != p2:
                    if not test2:
                        x -= xdis
                        y -= ydis

                
                    while x >= 0 and y >= 0 and x < 50 and y < 50:
                        uniq |= {( x, y )}
                        x = x-xdis
                        y = y-ydis
                        if not test2: break

    print(len(uniq))


print("took %s seconds" % (time.time() - start_time))