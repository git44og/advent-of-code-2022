def getGroup(line, i):
    return line[i:i+4]

def hasDuplicates(group):
    return len(set(list(group)))<len(group) #len(group)

# with open('05/sample.txt') as f:
with open('06/task.txt') as f:
    lines = f.readlines()

score = 0
for line in lines:
    line = line.rstrip()

for i in range(0, len(line)-3):
    if not (hasDuplicates(getGroup(line, i))):
        print(i+4)
        exit()


# mylist = ['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']
# myset = set(mylist)