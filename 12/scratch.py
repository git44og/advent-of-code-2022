from Item import Item

item = Item(98, True)

def check():
    print('div:{} rem:{} actual:{}'.format(item.dividable(23), item.remainder[23], (item.value % 23)))
    # print(item.dividable(23))
    # print(item.value % 23)

#['*19', '+3', '+6', '*19', '+3', '+6', '*19']
item.mult(19)
check()
item.add(3)
check()
item.add(6)
check()
item.pow()
check()
item.mult(19)
check()
item.add(3)
check()
item.add(6)
check()
item.mult(19)
check()
