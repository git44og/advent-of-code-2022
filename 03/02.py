def getChar(lines):
    for c in lines[0]:
        if c in lines[1] and c in lines[2]:
            return c

def getScore(c):
    if ord(c) > 96:
        return ord(c) - 96
    return ord(c) - 38

with open('03/02 task.txt') as f:
    lines = f.readlines()

score = 0
i = 0
group = [0,0,0]
for line in lines:
    group[i] = line.strip()
    if i == 2:
        c = getChar(group)
        score += getScore(c)
        i = 0
    else:
        i += 1
    

print (score)