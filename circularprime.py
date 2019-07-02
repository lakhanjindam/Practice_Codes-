#PF-Assgn-57
def check_prime(number):
    rotations_list = rotations(number)
    out = []
    for num in rotations_list:
        if num > 2:

            #it will chekc for complete range if number is divisible then it'll not append
            for i in range(2, num):
                if num%i==0:
                    break
            #this will run after for loop is fully executed and 
            # number which remained undivisible gets appended to "out" list
            else:
                out.append(num)

        else:
            out.append(num)

    if rotations_list == out:
        return True
    else:
        return False

def rotations(num):
    temp = str(num)
    out = [num]
    if len(temp)==1:
        return out
    elif len(temp)==2:
        temp = (temp[-1:]+temp[:1])
        out.append(int(temp))
    else:
        for i in range(1,len(temp)):
            temp = (temp[-2:]) + (temp[:1])
            out.append(int(temp))


    return out

def get_circular_prime_count(limit):
    out = []
    for i in range(2,limit):
        if check_prime(i):
            out.append(i)

    return len(out)
#Provide different values for limit and test your program
print(rotations(454))
print(get_circular_prime_count(1000))
