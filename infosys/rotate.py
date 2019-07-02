#PF-Prac-16
def rotate_list(input_list,n):
    
    output_list = []
    # it will return the last n elements
    for i in range(len(input_list)-n, len(input_list)):
        output_list.append(input_list[i])

    #it will return the first len(list)-n elements
    for j in range(0, len(input_list)-n):
        output_list.append(input_list[j])

    
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)