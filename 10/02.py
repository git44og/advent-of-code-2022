queue = []
valX = 1
cycle = 0
stopCycles = [20, 60, 100, 140, 180, 220]
drawPos = 0
drawLine = ''

stepsToComplete = 0
bufferAdd = 0

def makeNoop(line):
    global queue
    if line == 'noop':
        queue.append(0)

def makeAdd(line):
    global queue
    if line == 'noop':
        return
    method, value = line.split(' ')
    queue.append(0)
    queue.append(int(value))

def process():
    global queue, valX, cycle
    valX += queue[0]
    # print('                         c{} change:{} x:{}'.format(cycle, queue[0], valX))
    queue = queue[1:]


def getCycle():
    global cycle, valX, stopCycles
    # stopCycles = [2, 5]
    
    if cycle in stopCycles:
        stopCycles = stopCycles[1:]
        return valX * cycle
    return 0

def draw():
    global valX, drawPos, drawLine, cycle
    drawPos = ((cycle-1) % 40)
    if drawPos >= valX-1 and drawPos <= valX+1:
        sign = '#'
    else:
        sign = '.'
    drawLine = '{}{}'.format(drawLine, sign)
    # print('c:{} x:{} pos:{} {}'.format(cycle, valX, drawPos, sign))
    if drawPos == 39:
        print(drawLine)
        drawLine = ''
    
    

signal = 0

with open('10/task.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()

    makeNoop(line)
    makeAdd(line)
#print(queue)

for i in range(0, len(queue)):
    cycle += 1

    # signal += getCycle()
    draw()
    
    process()
    #print('{}. val:{} q:{}'.format(cycle, valX, signal))

print(signal)