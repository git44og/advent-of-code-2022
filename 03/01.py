def getCompartments(line):
    line = line.strip()
    middle = int(len(line)/2)
    return [
        line[0:middle],
        line[middle:]
    ]

def getChar(line1, line2):
    for c in line1:
        if c in line2:
            return c

def getScore(c):
    if ord(c) > 96:
        return ord(c) - 96
    return ord(c) - 38

with open('03/01 task.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    compartments = getCompartments(line)
    c = getChar(compartments[0], compartments[1])
    score += getScore(c)

print (score)