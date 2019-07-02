# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
n = int(input())
for i in range(n):
    s = input()

    even = ""
    odd = ""
    for i,j in enumerate(s):
        if(i%2==0):
            even+=s[i]
        else:
            odd+=s[i]


    print(even+" "+odd)
'''

#2 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    rev = arr[::-1]

    #whenever want to convert int list to string, first convert each element of list into str type
    string = [str(i) for i in rev ]
    print(string)
    #then simply use join 
    print(" ".join(string))

#3

n = int(input())
#now name_number has name and number of person
name_number = [input().split(" ") for i in range(n)]

#this will assign key as first value of input and value as second to the dict phone_book.
phone_book = {k: v for k,v in name_number}
while True:
    try:
        name = input()
        if name in phone_book:
            print("{0}={1}".format(name, phone_book[name]))
            break
        else:
            print("Not found")
    except:
        break

#4
