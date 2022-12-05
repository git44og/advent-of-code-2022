stacks = []
stackLine = []
moveLine = []
stackNum = 0

def isNumberLine(line):
    return line[0:10] == ' 1   2   3'

def isStackline(line):
    return len(line) > 3 and (line[0] == '[' or line[0:3] == '   ')

def isMoveLine(line):
    return line[0:4] == 'move'

def process(line, move):
    moveElements = move.split(' ')
    items = int(moveElements[1])
    fromStack = int(moveElements[3])-1
    toStack = int(moveElements[5])-1

    tmp = []
    for i in range(0,items):
        moveItem = stacks[fromStack].pop()
        tmp.append(moveItem)
    stacks[toStack] += list(reversed(tmp))

# with open('05/sample.txt') as f:
with open('05/02 task.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    line = line.rstrip()
    if isStackline(line):
        stackLine.append(line)
    if isMoveLine(line):
        moveLine.append(line)
    if isNumberLine(line):
        stackNum = int((len(line)+1)/3)

for i in range(0, stackNum):
    stacks.append([])

for stackConfig in stackLine:
    for i in range(0, stackNum):
        col = (i*4)+1
        if col > len(stackConfig):
            continue
        if stackConfig[col] != ' ':
            stacks[i].append(stackConfig[col])

for i in range(0, stackNum):
    stacks[i] = list(reversed(stacks[i]))

for move in moveLine:
    process(line, move)

result = ''
for i in range(0, stackNum):
    if len(stacks[i]) > 0:
        result = '{}{}'.format(result, stacks[i].pop())
    else:
        result = '{} '.format(result)

print (result)