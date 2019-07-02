
li = [1,2,3,5,42,45,21,78]


#it takes two args function and iterable like list, tuple
#returns the list of elements which is divisible by 2
s = list(filter(lambda x: x%2==0, li))
print(s)

#2
#returns only the elements which is less than zero
#if map is used it'll return true and false of each element in the list.
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
less_than_zero1 = list(map(lambda x: x < 0, number_list))
print(less_than_zero)
print(less_than_zero1)