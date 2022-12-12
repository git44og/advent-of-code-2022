class Monkey:

    monkeyGroup = []

    queue = []

    operator = '+'
    type1 = 'old'
    type2 = '1'
    test = 1
    trueMonkeyId = 0
    falseMonkeyId = 0
    num = ''

    inspect = 0

    def __init__(self, num, monkeyGroup):
        self.num = num
        self.queue = list()
        self.monkeyGroup = monkeyGroup
        pass

    def setQueue(self, value):
        # print('queue {}'.format(self.num))
        elements = value.strip().split(',')
        for el in elements:
            self.queue.append(int(el.strip()))

    def itemLen(self) -> int:
        return len(self.queue)

    def setOperation(self, value):
        # print('setOperation {}'.format(self.num))
        elements = value.strip().split(' ')
        self.type1 = elements[2].strip()
        self.operator = elements[3].strip()
        self.type2 = elements[4].strip()

    def setTest(self, value):
        # print('setTest {}'.format(self.num))
        elements = value.strip().split(' ')
        self.test = int(elements[2])

    def setIfTrue(self, value):
        # print('setIfTrue {}'.format(self.num))
        elements = value.strip().split(' ')
        self.trueMonkeyId = int(elements[3])
        
    def setIfFalse(self, value):
        # print('setIfFalse {}'.format(self.num))
        elements = value.strip().split(' ')
        self.falseMonkeyId = int(elements[3])

    def getWorryLevel(self, item) -> int:
        # print('{}.{}.{}.{}'.format(item, self.type1, self.operator, self.type2))
        if self.type1 == 'old':
            var1 = item
        else:
            var1 = int(self.type1)
        if self.type2 == 'old':
            var2 = item
        else:
            var2 = int(self.type2)
        match self.operator:
            case '+':
                return int((var1 + var2) / 3)
            case '*':
                return int((var1 * var2) / 3)

    def popItem(self) -> int:
        if len(self.queue) == 0:
            return None
        item = self.queue[0]
        if len(self.queue) == 1:
            self.queue = []
        else:
            self.queue = self.queue[1:]
        return item
    
    def addToQueue(self, item):
        self.queue.append(item)

    def processItem(self):
        # global monkeyGroup
        item = self.popItem()
        self.inspect += 1
        worryLevel = self.getWorryLevel(item)
        # print(worryLevel)
        if worryLevel % self.test == 0:
            self.monkeyGroup[self.trueMonkeyId].addToQueue(worryLevel)
        else:
            self.monkeyGroup[self.falseMonkeyId].addToQueue(worryLevel)

    def getInspect(self) -> int:
        return self.inspect

    def __str__(self) -> str:
        print('{} {}'.format(self.num, len(self.queue)))
        # print('{} {} {} {} {} {}'.format(self.num, self.queue, self.test, self.type1, self.operator, self.type2))
