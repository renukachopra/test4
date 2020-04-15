def name_checker(name):
    flag = True
    while flag:
        if name == 'renuka':
            return('bingo')
            flag = False
        else:
            name = input('enter new name')
            continue

print(name_checker('rc'))

