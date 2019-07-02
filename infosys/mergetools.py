from collections import OrderedDict
'''def merge_the_tools(string, k):
    
    fisrt_half = string[:k+k]
    last_half = string[-k:]
    first = fisrt_half[:k]
    second = fisrt_half[-k:]

    print(''.join(OrderedDict.fromkeys(first)))
    print(''.join(OrderedDict.fromkeys(second)))
    print(''.join(OrderedDict.fromkeys(last_half)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)  

def merge_the_tools(S,K):
    temp = []
    len_temp = 0
    for item in S:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == K:
            print(''.join(temp))
            temp = []
            len_temp = 0


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)'''

n = int(input())
set1 = set(map(int,input().split(" ")))
num = int(input())
for i in range(num):
    operation_name, length = input().split()
    set2 = set(map(int,input().split(" ")))
    if operation_name == "intersection_update":
        set1.intersection_update(set2)
    elif operation_name == "update":
        set1.update(set2)

    elif operation_name == "symmetric_difference_update":
        set1.symmetric_difference_update(set2)

    elif operation_name == "difference_update":
        set1.difference_update(set2)
        
print(sum(set1))
