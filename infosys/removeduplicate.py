#PF-Assgn-60
from collections import OrderedDict
def remove_duplicates(value):

    #maintains the order of the string and removes duplicate values.
    return ''.join(OrderedDict.fromkeys(value))  

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))

'''
l = [9,2,1,1,13,4]
l1 = list(map(str, l))
print(''.join(l1))'''