import json

pairs = []

class Point:
    x = 0
    y = 0
    def __init__(self, pointStr):
        xStr, yStr = pointStr.split(',')
        self.x = int(xStr)
        self.y = int(yStr)
    def __str__(self) -> str:
        return '{},{}'.format(self.x, self.y)
    
class Path:

    def __init__(self, pathStr):
        self.path = []
        pointStrs = pathStr.strip().split(' -> ')
        for pointStr in pointStrs:
            self.path.append(Point(pointStr))

    def __str__(self) -> str:
        return ' > '.join(map(str, self.path))

    def isOnSegment(self, x, y, p1, p2) -> bool:
        if p1.x == p2.x and x == p1.x:
            if p1.y < p2.y:
                return y >= p1.y and y <= p2.y
            return y >= p2.y and y <= p1.y
        elif p1.y == p2.y and y == p1.y:
            if p1.x < p2.x:
                return x >= p1.x and x <= p2.x
            return x >= p2.x and x <= p1.x
        return False
    
    def isOnPath(self, x, y) -> bool:
        for i in range(0, len(self.path)-1):
            start = self.path[i]
            end = self.path[i+1]
            if self.isOnSegment(x, y, start, end):
                return True
        return False
    
class Cave:
    def __init__(self):
        self.paths = []
        self.sands = []
    
    def addPath(self, pathStr):
        self.paths.append(Path(pathStr))

    def addSand(self, sand):
        self.sands.append(sand)

    def hasRock(self, x, y) -> bool:
        for path in self.paths:
            if path.isOnPath(x, y):
                return True
        return False
    
    def hasSand(self, x, y) -> bool:
        # print(len(self.sands))
        for sand in self.sands:
            if sand.isSand(x, y):
                # print(str(sand))
                return True
        return False

    def __str__(self) -> str:
        return '\n'.join(map(str, self.paths))

class Sand:
    def __init__(self, x=500, y=0):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return '{},{}'.format(self.x, self.y)
    
    def isSand(self, x, y):
        return x == self.x and y == self.y
    
    def fall(self, cave) -> bool:
        x = self.x
        y = self.y+1
        if y > 200:
            print('too deep')
            return False
        if not cave.hasRock(x, y) and not cave.hasSand(x, y):
            self.y = y
            return True
        x = self.x-1
        if not cave.hasRock(x, y) and not cave.hasSand(x, y):
            self.y = y
            self.x = x
            return True
        x = self.x+1
        if not cave.hasRock(x, y) and not cave.hasSand(x, y):
            self.y = y
            self.x = x
            return True
        print('rest {}'.format(str(sand)))
        return False

cave = Cave()

with open('14/task.txt') as f:
    # lines = f.readlines()

    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        cave.addPath(line)

# while True:
for sandCount in range(0, 10000):
    sand = Sand()
    cave.addSand(sand)
    while sand.fall(cave):
        pass
    if sand.y >= 200:
        print(sandCount)
        exit()

exit()
for y in range(0, 11):
    row = []
    for x in range(493, 505):
        if cave.hasRock(x, y):
            row.append('#')
        elif cave.hasSand(x, y):
            row.append('o')
        else:
            row.append('.')
    print(''.join(row))