def calc(stone):
    str_stone = str(stone)
    if stone == 0:
        return [1]
    elif len(str_stone) % 2:
        return [stone * 2024]
    else:
        half = len(str_stone) // 2
        return [int(str_stone[:half]), int(str_stone[half:])]
    
stones = {}
for n in map(int, input().split()):
    stones[n] = stones.get(n, 0) + 1

for i in range(75):
    new = {}
    total = 0
    for stone, cnt in stones.items():
        for res in calc(stone):
            new[res] = new.get(res, 0) + cnt
            total += cnt
    stones = new

    if i in [24, 74]:print(total)