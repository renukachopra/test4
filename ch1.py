'''
WAP to print a message if the passed value is >5 or less than 5
a --> input
output --> greater/less/equal to 5
'''
def test_num():
    a = int (input('Enter your number:: '))
    if  a < 5:
        print("Less")
    elif a == 5:
        print("equal")
    else:
        print("Greater")


def test_num1(b):
    #a = int (input('Enter your number:: '))
    a = int(b)
    if a < 5:
        return "Less"
    elif a == 5:
        return "equal"
    else:
        return "Greater"


x = test_num1('10')
print('val of x',x)
