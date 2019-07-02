#PF-Prac-47
import re
def list_rotate(uniquecode_list):
    rotated_list=[]
    for i in range(len(uniquecode_list)):
        first,second = uniquecode_list[i].split("-")
        length = len(re.findall(r'[A-Z]',uniquecode_list[i]))
        for i in range(length):
            second = second[1:] + second[:1]

        uniquode = first[:length] + (second)
        rotated_list.append(uniquode)
    return rotated_list

#You may modify the below code for testing
n = int(input())
uniquecode_list= []
for i in range(n):
    val = input()
    uniquecode_list.append(val)
    
print(uniquecode_list)
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)