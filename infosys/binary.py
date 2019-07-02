a = int(input().strip())

#split the numbers if 0 is present and
#  we will get the consecutive one's if present

numbers = str(bin(a)[2:]).split('0')
print(numbers)

#find len of consecutive one's
length = [len(num) for num in numbers ]
max_len = max(length)
print(max_len)
