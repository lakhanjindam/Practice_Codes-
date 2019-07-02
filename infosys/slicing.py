'''marks = ["fa1", 80, "fa2", 85, "fa3", 95, "sas"]

#last four numbers

print(len(marks[-1]))
#prints first number of above result with concat of last number of marks(list)
report=marks[:1]+marks[5:]


print(report)

import re
temp = "indiaparker@ind.com"
temp1 = ""
if (re.search(r'@ind\.com', temp)):

    temp1 = re.sub(r'i\w+(\.com)', r'edu\1', temp)

print(temp1)

l = [1,2,3,4,5,7,8,9]
f = lambda x: (x*2)%3!=0
for item in l:
    if (not(f(item))):
        l.remove(item)

print(l)

a = "i am iam iiam"
print(a.count("am"))

def fun(n):
    if n<1:
        return 0
    elif n%2==0:
        return fun(n-1)
    else:
        return n + fun(n-2)

print(fun(10))


import re
str1 = "Encountered Error : error code E101"
if (re.search(r'E...r', str1)!=None):
    str2 = re.sub(r'E(\d{3})', r'#\1', str1)
    print(str2)

#PF-Tryout

#debug the below code

def print_star(rows):
    for i in range(0, rows):
        for j in range(0, i+1):
            print("* ", end="")

        print("\r")

print_star(10)

#alt

l = []
n = 5

# -1 for reverse pattern
for i in range(n+1, 1, -1):
    l.append("*"*i)

print("\n".join(l))

def func(a,b):
    try :
        c = int(a)
        b=c+"A"
        print(b)
    except TypeError:
        print("I")
    finally:
        print("IF")
try:
    func('R',13)
except ValueError:
    print("V")
finally:
    print("OF")

#PF-Prac-29
def exchange_list(number_list):
    
    mid  = int(len(number_list)/2)
    rev = number_list[::-1]
    
    number_list = rev[:mid] + number_list[:mid]
    
    return number_list
     
number_list=[10,20,30,40,50,60]
print(exchange_list(number_list))


#PF-Prac-4
def find_nine(nums):
    
    if len(nums) > 4:
        for i in nums[:4]:
            if i==9:
                return True
        return False
    elif(len(nums)<=4):
        for i in nums:
            if i==9:
                return True
        return False
    

nums=[1,9,4,5,6]
print(find_nine(nums))

#PF-Prac-15
def check_22(num_list):
    for i in range(len(num_list)):

        #if index i has reached the last index of list 
        # it means that it has not found any consecutive 2's in between and return False
        if i==len(num_list)-1:
            return False

        # checks current index and next index has the same value or not    
        elif num_list[i] == num_list[i+1]:
            return True
        

print(check_22([3,2,5,1,2,1,3,2]))'''


#PF-Prac-13
def close_number(num1,num2,num3):
    a = abs(num1 - num2)
    b = abs(num1 - num3)
    c = abs(num2 - num3)

    if(a==1):
        if(abs(num3-num1)>=2 and abs(num3-num2)>=2):
            print(True) 
 
    elif(b==1):
        if(abs(num2-num1)>=2 and abs(num2-num3)>=2):
            print(True)
    
    elif(c==1):
        if(abs(num1-num2)>=2 and abs(num1-num3)>=2):
            print(True) 
        
    elif(a==0 or b==0 or c==0):
        return ""
    else:
        return False 
    

(close_number(5,6,7))