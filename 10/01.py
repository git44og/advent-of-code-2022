valX = 1
cycle = 1
stopCycles = [20, 60, 100, 140, 180, 220]

def makeNoop(line):
    if line == 'noop':
        return 1
    return 0

def makeAdd(line):
    global valX
    if line == 'noop':
        return 0
    method, value = line.split(' ')
    if method != 'addx':
        return 0
    valX += int(value)
    return 2

def getCycle():
    global cycle, valX, stopCycles
    # stopCycles = [2, 5]
    
    if cycle+1 in stopCycles:
        stopCycles = stopCycles[1:]
        return valX * (cycle+1)
    if cycle in stopCycles:
        stopCycles = stopCycles[1:]
        return valX * cycle
    return 0



signal = 0

with open('10/task.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()

    cycle += makeNoop(line)
    cycle += makeAdd(line)
    c = getCycle()
    signal += c

    print('{}. x:{} c:{}'.format(cycle, valX, c))

print(signal)