'''
from 1 to 10 print no div by 2
'''
li=[]
def test1(x,y):
    for i in range (x,y):
        if i%2 == 0:
            li.append(i)
    return li

print (test1(1,10))

