dir = {'/': {}}
modeLS = False
path = []
score = 0

bestDir = ''
bestSize = 70000000

totalSpace = 0
freeSpace = 0
neededSpace = 8381165

def isCommand(line):
    return line[0:1] == '$'

def runLS(line):
    if line != '$ ls':
        return False
    return True

def runCD(line):
    if line[0:4] != '$ cd':
        return
    folder = line[5:]
    if folder == '..':
        path.pop()
    else:
        path.append(folder)

def getFolder(myPath):
    myFolder = dir
    for folder in myPath:
        myFolder = myFolder[folder]
    return myFolder

def addLS(line, folder):
    size, folderName = line.split(' ')
    folder = getFolder(path)
    if size == 'dir':
        folder[folderName] = {}
    else:
        folder[folderName] = int(size)

def getSize(myPath):
    myFolder = getFolder(myPath)
    if isinstance(myFolder, int):
        return myFolder
    else:
        size = 0
        for subFolder in myFolder:
            size += getSize(myPath+[subFolder])
        return size

def walkDirs(myPath):
    global score, bestDir, bestSize, neededSpace
    myFolder = getFolder(myPath)
    if not isinstance(myFolder, int):
        size = getSize(myPath)
        if size > neededSpace and size < bestSize:
            bestDir = '/'.join(myPath)
            bestSize = size
            print('{} {}'.format('/'.join(myPath), size)) 
            score += size
        for subFolder in myFolder:
            walkDirs(myPath+[subFolder])



with open('07/task.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    if isCommand(line):
        # modeLS = False
        modeLS = runLS(line)
        runCD(line)
    else:
        folder = getFolder(path)
        addLS(line, folder)

result = {}

totalSpace = getSize(['/'])
freeSpace = 70000000 - totalSpace
neededSpace = 30000000 - freeSpace

walkDirs(['/'])

print('total: {} \nfree:{} \nneeded:{} \nfolder:{} \nsize:{}'.format(totalSpace, freeSpace, neededSpace, bestDir, bestSize))





# mylist = ['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']
# myset = set(mylist)