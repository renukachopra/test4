import random
streak_count=0

for i in range(10000):
    l1 = []
    for experimentNumber in range(10):
        v = random.randint(0,1)
        l1.append(v)
    #print(l1[:-1])
    counter = 1
    for index,item in enumerate(l1[:-1]):
        if item == l1[index+1]:
            counter = counter + 1
            a = counter
            #print("value of item "+str(item)+" value of item[index+1]= "+str(l1[index+1])+"value of counter = " +str(counter) + "and a= "+ str(a)+" at index "+str(index))
            if a == 6:
                #print("Streak")
                counter=1
                a=1
                streak_count = streak_count+1
            else:
                pass
        else:
            #print('passing')
            continue
print("stk is",streak_count/100)








