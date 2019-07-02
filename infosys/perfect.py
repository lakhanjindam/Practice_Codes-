#PF-Assgn-59
def check_perfect_number(number):
    sum = 0
    for x in range(1, number):
        if number % x == 0:
            sum += x
    return sum == number
    
def check_perfectno_from_list(no_list):

    out = []
    for i in no_list:
        if check_perfect_number(i):
            out.append(i)
        else:
            pass
    return out


perfectno_list=check_perfectno_from_list([18,6,4,2,1,8])
print(perfectno_list)