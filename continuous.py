import random
import math
def populate(k):
    '''populate a list L with k random numbers with random signs'''
    L=[] #initialise an empty list.
    for i in range(k):
        x=random.randint(1,10000000) #pick a random big number
        x=x*(random.choice([-1,1])) #assign a +1/-1 to it randomly
        L.append(x)
    return L

def sum(L,i,j):
    '''computes the sum of the numbers from L[i]....L[j]'''
    answer=0
    for k in range(i,j+1):
        answer=answer+L[k]
    return answer

def find_continous(L):
    '''This will find a continuous chunk in L that adds to a number that is
    maximum.'''
    maximum=(math.inf)*(-1)
    for i in range(len(L)):
        for j in range(i,len(L)):
            total=sum(L,i,j)
            if total>maximum:
                maximum=total
                ans=(i,j,total)
    return ans
    

    



