s = "lajsajsljalsjlasj"
li = []
for i in s:
    li.append(i)

print(li)
count = 0
li2  = []
for j in li:
    if(count%2==0):
        li2.append(j)
    count+=1

print(''.join(li2))
