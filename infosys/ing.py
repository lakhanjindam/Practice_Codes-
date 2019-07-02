#PF-Prac-1
def add_string(str1):

    #for getting last three letters of string
    string = str1[-3:]
    if(string == "ing" and str1!="is"):
        str1 = str1+"ly"
    elif(string != "ing" and str1!="is"):
        str1 = str1 + "ing"
    elif(0<len(str1)<3):
        str1 = str1+"ing"
    elif(str1 == "is"):
        return "is"
        

  
    return str1

str1=input()
print(add_string(str1))