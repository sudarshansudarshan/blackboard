import random

def disp(m,n):
    '''
    This code will type all possible numbers of the form (i,j) ranging from (0,0)
    to (9,4)
    '''
    for i in range(10):
        for j in range(5):
            print("(",i,j,")",end="")


def average_hundred_random(n):
    '''Consider n random numbers in the range of 1 to 1M and find its average'''
    L=[]
    for i in range(n):
        #append n random numbers into L.
        L.append(random.randint(1,1000*1000))
    #find the average
    total=0
    for i in range(n):
        total=total + L[i]
    average=total/n
    print(L)
    print("Average is : ",average)


