'''
WAP to find out even or odd number between any range which will return square and cube respectively
'''

def sqrt(x):
    a = x*x

    return a

#print(sqrt(5))

def cubes(y):
    b = y*y*y

    return b
#print(cubes(3))

def odd_even(start_range,end_range):
    l1 = []
    l2 = []
    for z in range(start_range,end_range):
        if z%2 == 0:
            c = sqrt(z)
            l1.append(c)
            #print(l1)
        else:
            c = cubes(z)
            l2.append(c)
            #print(l2)
    return l1,l2



print(odd_even(2,9))

