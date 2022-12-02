elves = []
currentElve = 0

with open('01.1 task.txt') as f:
    lines = f.readlines()
    
for line in lines:
    line = line.strip()
    if line == '':
        elves.append(currentElve)
        currentElve = 0
    else:
        currentElve += int(line)
elves.append(currentElve)

ordered = sorted(elves)
ordered.reverse()
print(sum(ordered[:3]))
# print (reversed(sorted(elves)))