def num2words(num):

    nums_20_90 =['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    nums_0_19 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight',"Nine", 'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    nums_dict = {100:"hundred"}

    #for numbers in between 0  and 19 both inclusive
    # we just map the input number to idexes of the nums_0_19 list
    
    if num < 20:
        return nums_0_19[num] 
    
    # num//10 because it returns float value so floor division for integer value
    if num < 100:
        return (nums_20_90[num//10]) + ('' if num%10==0 else ' ' + nums_0_19[num%10])

    if 100<=num<1000:
        return nums_0_19[hundreds] + " hundred" + var
        

print(num2words(200))