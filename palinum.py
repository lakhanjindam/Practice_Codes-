def reverse(num):
    temp = str(num)
    rev = temp[::-1]
    return int(rev)

def ispalin(num):
    return num == reverse(num)

def addandreverse(num):
    rev_num = 0
    while num > 0:
        rev_num = reverse(num)

        num+=rev_num

        if(ispalin(num)):
            print(num)
            break
       

addandreverse(212121)
        

    