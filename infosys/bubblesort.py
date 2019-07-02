#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps=0
for i in range(n):

 
        # Last i elements are already in place
    for j in range(0, n-i-1):
 
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if a[j] > a[j+1] :
            a[j], a[j+1] = a[j+1], a[j]
            swaps+=1




print("Array is sorted in {0} swaps.".format(swaps))
print("First Element: {0}".format(a[0]))
print("Last Element: {0}".format(a[n-1]))



