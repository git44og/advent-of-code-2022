import math

trees = []
score = 0


def getLeft(x, y):
    global trees
    row = trees[y][0:x]
    row.reverse()
    return row

def getRight(x, y):
    global trees
    return trees[y][x+1:]

def getTop(x, y):
    global trees
    row = []
    for i in range(0,y):
        row.append(trees[i][x])
    row.reverse()
    return row

def getBottom(x, y):
    row = []
    for i in range(y+1,len(trees)):
        row.append(trees[i][x])
    return row

def getDist(row, height):
    dist = 1
    for treeHeight in row:
        if treeHeight < height:
            dist += 1
        else:
            return dist
    dist -= 1
    return dist



with open('08/task.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    trees.append(list(line))



score = 0
sizeH = len(trees)
sizeW = len(trees[0])

# x=2
# y=2
# height = trees[y][x]
# print(getLeft(x,y))
# print(getDist(getLeft(x,y),height))
# print(getRight(x,y))
# print(getDist(getRight(x,y),height))
# print(getTop(x,y))
# print(getDist(getTop(x,y),height))
# print(getBottom(x,y))
# print(getDist(getBottom(x,y),height))


for y in range(1, len(trees)-1):
    row = trees[y]
    for x in range(1, len(row)-1):
        height = row[x]
        sceenicScore = getDist(getLeft(x,y),height) * getDist(getRight(x,y),height) * getDist(getTop(x,y),height) * getDist(getBottom(x,y),height)
        if sceenicScore>score:
            # print('{} {}'.format(x,y))
            score = sceenicScore
print(score)