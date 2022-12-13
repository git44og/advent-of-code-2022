import json
import functools

pairs = [
    [[2]],
    [[6]]
    ]

with open('13/task.txt') as f:
    # lines = f.readlines()

    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        if line == '':
            continue
        pairs.append(json.loads(line))

def checkInt(left, right) -> int:
    if left < right:
        return 1
    if right < left:
        return -1
    return 0

def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        # print('compare {} {}'.format(left, right))
        return checkInt(left, right)
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    for i in range(0, min(len(left), len(right))):
        comparison = compare(left[i], right[i])
        if comparison != 0:
            return comparison
    # print('list')
    return compare(len(left), len(right))


sortPairs = list(reversed(sorted(pairs, key=functools.cmp_to_key(compare))))
# print(sortPairs)

score = 1
for i in range(0, len(sortPairs)):
    if compare([[2]], sortPairs[i]) == 0:
        score *= i + 1
    if compare([[6]], sortPairs[i]) == 0:
        score *= i + 1
print (score)