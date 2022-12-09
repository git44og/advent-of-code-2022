import math

start = [0,0]
head = start
tail = start
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
    global head
    head = [head[0]+vector[0], head[1]+vector[1]]

def shouldMove(diff):

    return abs(diff[0]) > 1 or abs(diff[1]) > 1


def normalize(i):
    if i>0:
        return 1
    elif i<0:
        return -1
    return 0

def moveTail():
    global head, tail
    diff = [head[0]-tail[0], head[1]-tail[1]]
    if not shouldMove(diff):
        return
    if diff[0] == 0:
        tail[1] += normalize(diff[1])
    elif diff[1] == 0:
        tail[0] += normalize(diff[0])
    else:
        tail[0] += normalize(diff[0])
        tail[1] += normalize(diff[1])






with open('09/task.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    vector, steps = getTask(line)
    for i in range(0, steps):
        moveHead(vector)
        moveTail()
        coord = '{}|{}'.format(tail[0],tail[1])
        pos[coord] = 1
        # diff = [head[0]-tail[0], head[1]-tail[1]]
        # print('head:{}-{}   tail:{}-{}   diff:{}-{}'.format(head[0],head[1],tail[0],tail[1],diff[0],diff[1]))

print(len(pos))
