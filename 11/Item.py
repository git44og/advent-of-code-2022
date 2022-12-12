class Item:
    value = 0
    initvalue = 0
    remainder = {}
    log = []
    logVal = []
    calcValue = False
    def __init__(self, value, calcValue = False):
        self.initvalue = value
        self.value = value
        self.remainder = {
            2: 0,
            3: 0,
            5: 0,
            7: 0, 
            11: 0,
            13: 0,
            17: 0,
            19: 0,
            23: 0,
        }
        self.log = []
        self.logVal = []
        self.calcValue = calcValue

        for key in self.remainder:
            self.remainder[key] = value % key
        print(value)
        print(self.remainder)
    
    def add(self, value):
        # print('{}={}*{}'.format(self.value + value, self.value, value))
        if self.calcValue:
            self.value += value
            self.logVal.append(self.value)
        self.log.append('+{}'.format(value))
        for key in self.remainder:
            self.remainder[key] = (self.remainder[key] + value) % key
    
    def mult(self, value):
        # print('{}={}*{}'.format(self.value * value, self.value, value))
        if self.calcValue:
            self.value = self.value * value
            self.logVal.append(self.value)
        self.log.append('*{}'.format(value))
        for key in self.remainder:
            self.remainder[key] = (self.remainder[key] * value) % key
    
    def pow(self):
        # print('{}={}*{}'.format(self.value * value, self.value, value))
        if self.calcValue:
            self.value = self.value * self.value
            self.logVal.append(self.value)
        self.log.append('^2'.format())
        for key in self.remainder:
            self.remainder[key] = (self.remainder[key] * self.remainder[key]) % key
    
    def dividable(self, value) -> bool:
        res1 = self.value % value == 0
        res2 = self.remainder[value] == 0
        if res1 != res2:
            # print('divider %{} init {} % {} remainder {} log {}'.format(value, self.initvalue, self.value % value, self.remainder, self.log))
            # print('logVal {}'.format(self.logVal))
            # exit()
            pass
        # return self.value % value == 0
        return self.remainder[value] == 0

    def __str__(self) -> str:
        # desc = 'i.{}'.format(self.initvalue)
        desc = '({}){}'.format(self.value, self.remainder[23])
        # for key in self.remainder:
        #     desc = '{} {}:{}'.format(desc, key, self.dividable(key))
        return desc
        # print('{} {} {} {} {} {}'.format(self.num, self.queue, self.test, self.type1, self.operator, self.type2))
