# For removing duplicates values in list
'''l = list(map(int, input().split(",")))
print(l)
li = []
for i in l:
    if i not in li:
        li.append(i)

print(li)'''

#For intersection of lists
'''li1 = [1,23,12,45,67,31,43]
li2 = [23,56,32,45,68,90,98]
set1 = set(li1)
set2 = set(li2)
set1 &= set2
print(list(set1))'''

# Enumeration of list
# enumertae returns index and value of list
'''li1 = [12,34,21,45,121,67]
enum = enumerate(li1)
for i,j in enum:
        #excluding these positions all positions value is printed
    if i not in (2,3,5):
        print(j)'''

'''
li = [12,3,54,215,65,21]
x = [j for i,j in enumerate(li) if(i%2!=0)]
print(x)'''

'''
import random
print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 10))'''

#binary search
'''
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print (bin_search(li,11))
print (bin_search(li,12))'''

#fibonacci series
'''def fibo_series(n):

    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo_series(n-1)+fibo_series(n-2)

n = int(input())
x = [str(fibo_series(i)) for i in range(0,n+1) ]
print(','.join(x))'''


