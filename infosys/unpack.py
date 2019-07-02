from itertools import product

a = list(map(int, input().split()))

b = list(map(int, input().split()))


print (*product(a,b))


#syncing elements of two list i.e 1st elem of one list with 1st elem of another list.
a = [12,21,3,41,21,312,11]
b = [23,67,8,34,89,12]

for i,j in zip(a,b):
    print("list1 : {0}, list2: {1}".format(i,j))


