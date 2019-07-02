#PF-Prac-7
def seed_no(number,ref_no):
    string = str(number)
    res = number*1
    for i in string:
        res*=int(i)

    if (res)==ref_no:
        return True
    else:
        return False

number = 221
ref_no = 738
print(seed_no(number, ref_no))