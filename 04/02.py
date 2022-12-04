def getRangeCodes(line):
    return line.strip().split(',')

def getRange(rangeLine):
    start, end = rangeLine.split('-')
    return range(int(start), int(end)+1)

def getContains(range1, range2):
    for i in range1:
        if i in range2:
            return True
    return False

with open('04/02 task.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    rangeCode = getRangeCodes(line)
    pairRange = [
        getRange(rangeCode[0]),
        getRange(rangeCode[1]),
    ]
    if getContains(pairRange[0], pairRange[1]) or getContains(pairRange[1], pairRange[0]):
        score += 1

    
    
print (score)