import math

start = [0,0]
ropeLength = 10
rope = []
for i in range(0, ropeLength):
    coord = [start[0], start[1]]
    rope.append(coord)
pos = {}

def getTask(line):
    direction, steps = line.split(' ')
    vectorBase = {
        'R': [1,0],
        'L': [-1,0],
        'U': [0,-1],
        'D': [0,1],
    }
    return vectorBase[direction], int(steps)

def moveHead(vector):
    global rope
    rope[0] = [rope[0][0]+vector[0], rope[0][1]+vector[1]]

def shouldMove(diff):
    return abs(diff[0]) > 1 or abs(diff[1]) > 1


def normalize(i):
    if i>0:
        return 1
    elif i<0:
        return -1
    return 0

def moveKnot(ropePos):
    global rope
    diff = [
        rope[ropePos-1][0]-rope[ropePos][0], 
        rope[ropePos-1][1]-rope[ropePos][1]]
    if not shouldMove(diff):
        return
    if diff[0] == 0:
        rope[ropePos][1] = rope[ropePos][1] + normalize(diff[1])
    elif diff[1] == 0:
        rope[ropePos][0] = rope[ropePos][0] + normalize(diff[0])
    else:
        rope[ropePos][0] = rope[ropePos][0] + normalize(diff[0])
        rope[ropePos][1] = rope[ropePos][1] + normalize(diff[1])

def printRope():
    global rope, ropeLength
    str = ''
    for i in range(0, ropeLength):
        str = '{}.({}|{})'.format(str, rope[i][0], rope[i][1])
    print(str)


def showGrid():
    global rope, ropeLength
    print('knot-2:{} {}'.format(rope[1][0], rope[1][1]))
    for y in range(0,6):
        thisRow = []
        for x in range(0,6):
            for i in range(1, ropeLength+1):
                thisRow.append('.')
                if rope[ropeLength - i][0] == x and rope[ropeLength - i][1] == y:
                    thisRow[x] = '{}'.format(ropeLength - i)
        print(''.join(thisRow))
    print()

    for i in range(0, ropeLength):
        print('{} {} {}'.format(i, rope[i][0], rope[i][1]))
            

with open('09/task.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    vector, steps = getTask(line)
    for i in range(0, steps):
        moveHead(vector)
        for j in range(1, ropeLength):
            moveKnot(j)
        coord = '{}|{}'.format(rope[9][0],rope[9][1])
        pos[coord] = 1

        # showGrid()


print(len(pos))
