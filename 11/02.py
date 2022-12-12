from Monkey2 import Monkey
# for i in range(0,61):
#     print('{} {}'.format(i, i%13))
# exit()
monkeyGroup = []

def pm():
    for monkey in monkeyGroup:
        print(monkey)
        # print(monkey.num)
        # print('{} {}'.format(monkey.num, monkey.queue))
        # print(monkey.test)



with open('11/task.txt') as f:
    lines = f.readlines()

monkeyId = -1
monkey = None

for line in lines:
    # pm()
    line = line.rstrip()
    if line[0:6] == 'Monkey':
        monkeyId += 1
        monkey = Monkey(monkeyId, monkeyGroup)
        # print(monkeyId)
        monkeyGroup.append(monkey)
        continue
    if line != '':
        statement, value = line.split(':')
        if statement.strip() == 'Starting items':
            monkeyGroup[monkeyId].setQueue(value)
        if statement.strip() == 'Operation':
            monkeyGroup[monkeyId].setOperation(value)
        if statement.strip() == 'Test':
            monkeyGroup[monkeyId].setTest(value)
        if statement.strip() == 'If true':
            monkeyGroup[monkeyId].setIfTrue(value)
        if statement.strip() == 'If false':
            monkeyGroup[monkeyId].setIfFalse(value)

# pm()

for round in range(0,10000):
    for monkeyId in range(0, len(monkeyGroup)):
        monkey = monkeyGroup[monkeyId]
        itemNum = monkey.itemLen()
        for item in range (0, itemNum):
            monkey.processItem()
    print('round {}'.format(round+1))
    # pm()

inspect = []
for monkey in monkeyGroup:
    inspect.append((monkey.num, monkey.inspect))


inspect = sorted(inspect, key=lambda x: -x[1]) 
print(inspect)
print(inspect[0][1] * inspect[1][1])
# print(monkeyGroup[0].operator)
# print(signal)