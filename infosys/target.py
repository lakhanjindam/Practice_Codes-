#PF-Prac-36
def find_target_positions(input_string, target_word):
    target_list=[]
    list1 = input_string.split()
    for i in range(len(list1)):
        if list1[i]==target_word:
            target_list.append(i)
        
    return target_list

def find_inverted_index(input_string):
    target_dict={}
    list1 = input_string.split()
    for i in range(len(list1)):
        target_dict[list1[i]] = find_target_positions(input_string,list1[i])
        


    
    return target_dict
    
    
input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)