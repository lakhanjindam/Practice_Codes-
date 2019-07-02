import re
r = "2dsldsl"
str1 = ""
#to find string has digits or not
#re.compile coverts it into a pattern
reg = re.compile('[0-9]')
if len(re.findall(reg, r)) >= 1:

    if(r.startswith("-")):
        str1+="-"
    str1 = str1+''.join(x for x in r if x.isdigit())
    print(str1)
else:
    print("No digits")