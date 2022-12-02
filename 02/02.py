def getInputs(line):
    return [line[0],line[2]]

def getOwnInput(input):
    hand = {'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    },
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }}
    return [
        input[0],
        hand[input[1]][input[0]],
        ]

def gameScore(input):
    scoring = {'X': {
        'A': 3,
        'B': 0,
        'C': 6,
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0,
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3,
    }}
    return scoring[input[1]][input[0]]

def handScore(input):
    scoring = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    return scoring[input[1]]

# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors

with open('02/02 task.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    line = line.strip()
    input = getInputs(line)
    newInput = getOwnInput(input)
    score += handScore(newInput) + gameScore(newInput)

print (score)