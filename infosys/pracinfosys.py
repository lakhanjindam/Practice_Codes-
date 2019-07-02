#PF-Prac-37
def sum_of_list(num_list): 
    
    lst = []
    lst = num_list
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0] + sum_of_list(lst[1:])

num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)

#2

#PF-Prac-26
def check_occurence(string):
    string = string.lower()
    mat = string.count("mat")
    jet = string.count("jet")
    
    if(mat==jet):
        return True
    else:
        return False
        
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))

