import random
import numpy
def generate(n):
    """Generates n random numbers from 1 to a billion range"""

    L=[]
    for i in range(n):
        L.append(random.randint(1,1000))
    return L


def balance(U):
    """I consider the list U and create a left and right wing L and R with
    equal elements. Do this u.a.r and then find the mean of L and R, display
    the mean of L and R as well as the difference of their mean"""
    random.shuffle(U) #Shuffle the entries in U
    L=U[:len(U)//2]
    R=U[len(U)//2:]
    L_mean=numpy.mean(L)
    R_mean=numpy.mean(R)
    diff=abs(L_mean-R_mean)
    return L_mean,R_mean,diff

U=generate(100)
print(balance(U))



    


