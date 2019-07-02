#PF-Prac-10
def string_both_ends(input_string):
    if(len(input_string)>2):
        return input_string[:2] + input_string[(len(input_string)-2):]

    elif(len(input_string)==2):
        return input_string[:2] + input_string[:2]

    else:
        return -1

        
input_string="w3w"
print(string_both_ends(input_string))