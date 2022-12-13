with open('12/task.txt') as f:
    lines = f.readlines()

map = []
visited = []
currentVisited = []

class Step:

    previous = None
    num = 0
    x = 0
    y = 0
    map = None

    def __init__(self, previous, num, x, y, map, goal):
        self.previous = previous
        self.num = num
        self.x = x
        self.y = y
        self.map = map
        self.goal = goal

        if self.isGoal():
            print(self)
            self.printPath()
            exit()
    
    def printPath(self):
        path = []
        pre = self
        while pre != None:
            path.append('x:{} y:{} h:{}'.format(pre.x, pre.y, map[pre.y][pre.x]))
            pre = pre.previous
        print('\n'.join(path))
        


    def isGoal(self) -> bool:
        return self.x == self.goal['x'] and self.y == self.goal['y']

    def isValid(self) -> bool:
        global visited
        pos = '{}-{}'.format(self.x, self.y)
        if pos in visited:
            return False
        return True

    def getNeighbours(self) -> list:
        neightbours = []
        if self.x > 0:
            neightbours.append({'x': self.x-1, 'y': self.y})
        if self.x < len(self.map[0])-1:
            neightbours.append({'x': self.x+1, 'y': self.y})
        if self.y > 0:
            neightbours.append({'x': self.x, 'y': self.y-1})
        if self.y < len(self.map)-1:
            neightbours.append({'x': self.x, 'y': self.y+1})
        return neightbours
        
    def getNext(self) -> list:
        global visited

        if not self.isValid():
            return []

        next = []
        neighbours = self.getNeighbours()
        currentHeight = self.map[self.y][self.x]

        for neighbour in neighbours:
            nextHeight = self.map[neighbour['y']][neighbour['x']]
            if nextHeight - currentHeight <= 1:
                next.append(Step(self, self.num+1, neighbour['x'], neighbour['y'], self.map, self.goal))
        if len(next) > 0:
            pos = '{}-{}'.format(self.x, self.y)
            visited.append(pos)

        return next
    
    def __str__(self) -> str:
        return 'num:{} x:{} y:{}'.format(self.num, self.x, self.y)


def height(c):
    if c == 'S':
        return ord('a')-97
    if c == 'E':
        return ord('z')-97
    return ord(c)-97

start = {}
goal = {}
for line in lines:
    line = line.strip()
    if line.find('S') != -1:
        start = {'x': line.find('S'), 'y':len(map)}
    if line.find('E') != -1:
        goal = {'x': line.find('E'), 'y':len(map)}
    row = []
    for i in range(0, len(line)):
        row.append(height(line[i]))
    map.append(row)

print (start)
print (goal)
step = Step(None, 0, start['x'], start['y'], map, goal)
current = [step]
round = 0
for i in range(0,1000):
# while True:
    next = []
    for thisStep in current:
        next += thisStep.getNext()
    current = next
    round += 1
    # visited += currentVisited
    # print(len(visited))
    print('{} num:{}'.format(round, len(next)))
# print(start)
# print(map)

# print(visited)

def printAll():
    for y in range(0, len(map)):
        row = []
        for x in range(0, len(map[0])):
            pos = '{}-{}'.format(x, y)
            if pos in visited:
                row.append('X')
            else:
                row.append('.')
        print(''.join(row))

# printAll()