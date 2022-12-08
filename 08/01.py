import math

trees = []
score = 0


def getLeft(x, y):
    global trees
    return trees[y][0:x]

def getRight(x, y):
    global trees
    return trees[y][x+1:]

def getTop(x, y):
    global trees
    row = []
    for i in range(0,y):
        row.append(trees[i][x])
    return row

def getBottom(x, y):
    row = []
    for i in range(y+1,len(trees)):
        row.append(trees[i][x])
    return row




with open('08/task.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    trees.append(list(line))

x=2
y=2
print(getLeft(x,y))
print(getRight(x,y))
print(getTop(x,y))
print(getBottom(x,y))

score = 0
sizeH = len(trees)
sizeW = len(trees[0])

for y in range(1, len(trees)-1):
    row = trees[y]
    for x in range(1, len(row)-1):
        height = row[x]
        if height <= max(getLeft(x,y)) \
            and height <= max(getRight(x,y)) \
            and height <= max(getTop(x,y)) \
            and height <= max(getBottom(x,y)):
            score += 1

print(sizeH*sizeW - score)