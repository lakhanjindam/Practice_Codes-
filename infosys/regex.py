'''import re
def commandCount(commands):
    pattern = re.compile('^[a-z]\w*:/[a-z]+[0-9]+\[a-z]+$')

    for i in range(len(commands)):

        if re.match(pattern, commands[i]):
            return "1"
        else:
            return "0"

command = ["w\\//a/b", "w\\//a/b", "dada./dad/a"]
print(commandCount(command))

print(chr(97))'''

n = list(map(int,input().split()))
l1 = []
for i in range(n[0]):
    l1.append(list(map(int,input().split())))

print(l1)
#print(maximizeit(l1))