import time
data = []
start = time.time()
with open(0) as f:
    data = f.read().strip('\n').split('\n')


def can_make(result, rest, p2):
    rest = [*rest]
    if len(rest) == 1:
        return rest[0] == result

    last = rest.pop()

    if result % last == 0:
        possible_mul = can_make(result // last, rest, p2)
        if possible_mul: return 1
    else:
        possible_mul = False

    next_power_of_10 = 1
    while next_power_of_10 <= last:
        next_power_of_10 *= 10
    if p2 and (result - last) % next_power_of_10 == 0:
        possible_concat = can_make((result - last) // next_power_of_10, rest, p2)
        if possible_concat: return 1

    possible_add = can_make(result - last, rest, p2)
    return possible_add  # or possible_concat

r1 = 0
r2 = 0
for line in data:
    result, rest = line.split(': ')
    result = int(result)
    rest = [int(x) for x in rest.split()]
    if can_make(result, rest, 0):
        r1 += result
    if can_make(result, rest, 1):
        r2 += result
print(r1, r2)
print(time.time() - start)