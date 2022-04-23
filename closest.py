#Make this run faster.
#Superman!
import random
import pdb
#pdb.set_trace()

def sort_list(L):
    '''Sorts the element of L'''
    L.sort() #this is cheating. :)
    return L

def populate(L,k):
    '''This code extends the list L by k random elements'''
    for i in range(k):
        L.append(random.randint(1000000000,9999999999))
    return L


def element_remove(L,x):
    '''Remove the element x in L and return the resulting list'''
    n=len(L)
    for i in range(len(L)): #go till the end of the list
            if L[i]==x:     #until you find your x. The moment you find your x
                for j in range(i,n-1): #shift all elements by one unit to the
                    #right and ensure that x is deleted this way.
                    L[j]==L[j+1]
                L.pop()#This removes the last elment in the list. Note that
                #L[second last]==L[last]. We dont want this.
                break


def naive():
    '''We check if --->
    0: x is present or not
    1: insert x
    2: delete x if it is present
    3: Display the list L
    d
    '''
    L=[]
    while(1):
        print("Enter your choice: ")
        print("0: I-nsert an element")
        print("1: D-elete an element")
        print("2: L-ookup for an element")
        print("3: Print L")
        print("4: Extend L by k elements")

        d=int(input())
        if (d==4):
            print("Enter a value for k, by which you want to extend L")
            k=int(input())
            L=populate(L,k)
        if (d==3):
            print(L)
        if (d==0):
            print("Enter the element x which needs to be inserted")
            x=int(input())     
            L.append(x)
            L=sort_list(L)
        if (d==1):
            print("Enter the element x which needs to be deleted")
            x=int(input())     
            for i in range(len(L)):
                if (L[i]==x):
                    L=element_remove(L,x)
        if (d==2):
            print("Enter the element x which you want to lookup")
            x=int(input())
            flag=0
            for i in range(len(L)):
                if (L[i]==x):
                    print("Element found")
                    flag=1
                    break
            if flag==0:
                print("Element not found")
naive()
