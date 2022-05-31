import random
import math
def populate(k):
    '''populates a list L with k random numbers with random signs'''
    L=[] #initialise an empty list.
    for i in range(k):
        x=random.randint(1,100) #pick a random big number
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
    for i in range(len(L)):#i goes from 0 to n
        for j in range(i,len(L)): #j goes from i to n
            total=sum(L,i,j) 
            #8M calls for just 2000 elements.
            #if there are n elements, roughly we make 2n^2 calls.
            #if there are 1 M elements, we make 2*1T calls.
            #all that you need to know is the above line. 
            #2 Giga Hz = 2*(1000000000) operations per second.
            #Krishna's computer does 2B operations per second.
            #how much time will it take for him to do 2T operations?
            #Answer= 2T/2B seconds = 1000 seconds = 16 mins*100=1600mins=
            #30 hours = More than a day.
            if total>maximum:
                maximum=total
                ans=(i,j,total)
    return ans
    

    



