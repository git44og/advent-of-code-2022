import json

pairs = []

with open('13/task.txt') as f:
    # lines = f.readlines()

    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        if line == '':
            continue
        pair1 = json.loads(line)
        line = f.readline().strip()
        pair2 = json.loads(line)
        pairs.append([pair1, pair2])

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

score = 0
counter = 1
for pair in pairs:
    comparison = compare(pair[0], pair[1])
    if comparison == 1:
        score += counter
    counter += 1
    # print ('l:{} r:{} {}'.format(pair[0], pair[1], comparison))

print (score)