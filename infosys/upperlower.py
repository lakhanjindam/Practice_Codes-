#PF-Prac-11
def find_upper_and_lower(sentence):
    upper = 0
    lower = 0
    result_list = []
    
    for i in range(len(sentence)):
        if sentence[i].isupper():
            upper+=1
        elif sentence[i].islower():
            lower+=1
    result_list.append(upper)
    result_list.append(lower)
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))