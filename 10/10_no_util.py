grid = {}
for x,r in enumerate(open(0).read()):
    if r != "\n":
        grid[x] = int(r)

def count(loc, height, seen, i):
    if loc in grid and height == grid[loc]:
        if height == 9:
            if loc not in seen or i:
                seen[loc] = 1
                return 1
        tot = 0
        for d in [1, -1, 46, -46]:
            pos = loc+d
            if pos in grid:
                tot += count(pos, height+1, seen,i)
        return tot
    return 0

for i in 0,1:
    tot = 0
    for loc in grid:
        if grid[loc] == 0:
            tot += count(loc, 0,{},i)
    print(tot)