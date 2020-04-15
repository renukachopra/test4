def list_items(li=[]):
    '''

    accepts list as arguments

    returns string
       :param li:
    :return:
    '''

    #li.insert(-1,'and')
    a = ''.join(li)
    return a.upper()

#a = list_items(['i','a','e','o','u'])
#print(a)

def sort_str(x):
    l1 = []
    for i in x:
        l1.append(i)
    l1.sort()
    b= list_items(l1)
    return b


'''
created an empty list l1
looped through x:
    1st iter--> i ='s'
    li['s']
    li['s']
    li is returned
o/p ->[s]
    

'''

#print(sort_str('shubhanshu'))

'''
WAP which accepts one string and one string which has to replace the sting.
if the length of 2nd string is more  than 1st then don't replace for the length of string 1st only

renuka, shu -> shuuka
renuka, shubh -> shubha
renuka,shubhanshu->shubha

'''
def str_replace(a,b):
    l1 = []
    for i in a:
        l1.append(i)
    print("List one" ,l1)
    l2 = []
    for j in b:
        l2.append(j)
    print("List two", l2)

    if len(b)>len(a):
        print("NA")
        exit()
    else:
        for x,y in enumerate(l2):
            l1[x]= l2[x]
        e = list_items(l1)
    return e



print(str_replace('shubhanshu','renukabhyamasd'))















