#PF-Assgn-58
def validate_credit_card_number(card_number):
    str1 = (''.join(list(reversed(str(card_number)))))
    odd = []
    even = []
    for i in range(len(str1)):
        if i%2!=0:
            odd.append(int(str1[i]))
        else:
            even.append(int(str1[i]))

        
    summ = sum(odd) + sum(even)
    
    return summ%10

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result==0):
    print("credit card number is valid")
else:
    print("credit card number is invalid")