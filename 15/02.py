import json
import re

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return '{},{}'.format(self.x, self.y)
    def dist(self, point) -> int:
        return abs(self.x - point.x) + abs(self.y - point.y)

class Sensor(Point):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.range = 0
    def __str__(self) -> str:
        return '{},{} ({})'.format(self.x, self.y, self.range)
    def defineRange(self, beacon):
        self.range = self.dist(beacon)
    def pointsInRangeAt(self, row) -> list:
        radius = self.range - abs(self.y-row)
        points = []
        for i in range(self.x-radius, self.x+radius):
            points.append(Point(i, row))
        return points
    def endpointsInRangeAt(self, row) -> list:
        radius = self.range - min(abs(self.y-row), abs(row-self.y))
        if (radius <= 0):
            return None
        return sorted([self.x-radius, self.x+radius])

sensors = []

with open('15/task.txt') as f:
    # lines = f.readlines()

    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        p = re.compile('Sensor at x=([\-0-9]+), y=([\-0-9]+): closest beacon is at x=([\-0-9]+), y=([\-0-9]+)')
        m = p.match(line)
        sensor = Sensor(int(m.group(1)), int(m.group(2)))
        beacon = Point(int(m.group(3)), int(m.group(4)))
        sensor.defineRange(beacon)
        sensors.append(sensor)

for testY in range(0,4000000):
    if testY % 50000 == 0:
        print(testY)
    fields = []
    ranges = []
    # print ('calc')
    for sensor in sensors:
        subrange = sensor.endpointsInRangeAt(testY)
        if subrange != None:
            ranges.append(subrange)

    def rangeSortStart(elem):
        return elem[0]
    def rangeSortEnd(elem):
        return elem[1]


    ranges = sorted(ranges, key=rangeSortEnd)     
    ranges = sorted(ranges, key=rangeSortStart)     

    start = ranges[0][0]
    end = ranges[0][1]
    for i in range(1, len(ranges)):
        # print('{}|{}'.format(ranges[i][0], ranges[i][1]))
        if ranges[i][0] > end+1:
            fields.append([start, end])
            start = ranges[i][0]
            end = ranges[i][1]
        elif ranges[i][1] >= end:
            end = ranges[i][1]
    fields.append([start, end])

    elements = 0
    for subRange in fields:
        elements += subRange[1] - subRange[0]
    # print(ranges)

    if len(fields) > 1:
        print(testY)
        print(fields)

# for s in sensors:
#     print(str(s))
#     print(s.endpointsInRangeAt(10))

        # print(elements)
        x = fields[0][1]+1
        print('x:{} y:{} f:{}'.format(x, testY, x*4000000+testY))
