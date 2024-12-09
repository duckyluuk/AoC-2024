import time
start = time.time()

data = open(0).read()


def solve(data, part2):
    is_block = True
    blocks = []
    gaps = [[] for _ in range(10)]
    pos, b_id = 0, 0
    for size in data:
        size = int(size)
        if size:
            if is_block:
                if part2:
                    blocks.append([pos, b_id, size])
                else:
                    for i in range(size):
                        blocks.append([pos + i, b_id, 1])
                b_id += 1
            else:
                if part2:
                    gaps[size].append(pos)
                else:
                    for i in range(size):
                        gaps[1].append(pos+i)
        pos += size
        is_block = not is_block
    
    checksum = 0
    for b in range(len(blocks))[::-1]:
        bpos, bid, bsize = blocks[b]

        best_pos = bpos
        gpos = 999999
        glen = 0
        for i in range(10):
            if gaps[i] and i>=bsize:
                if gaps[i][0] < gpos:
                    gpos = gaps[i][0]
                    glen = i

        if glen:
            if gpos < bpos:
                best_pos = gpos
                gaps[glen].pop(0)
                if part2:
                    old = gaps[glen-bsize]
                    val = gpos+bsize

                    new = []
                    prev = 0
                    for item in old:
                        if prev <= val < item:
                            new.append(val)
                        new.append(item)
                        prev = item
                    
                    gaps[glen-bsize] = new
                    
            blocks[b][0] = best_pos

        checksum += bid*bsize*(2*best_pos + bsize-1)//2
    return checksum

print(solve(data, False))
print(solve(data, True))
print(time.time() - start)