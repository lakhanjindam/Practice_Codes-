from collections import Counter

a = "AAAaaaNN"
count = 1
res = []
for i in (range(len(a))):
    if(i==len(a)-1):
        res.append([a[i],count])

    elif(a[i]==a[i+1]):
        count+=1
    
    else:
        res.append([a[i],count])
        count=1

print((res))

out = []
for i in range(len(res)):
    for j in range(len(res[i])):
        out.append(res[i][j])

#first convert every elem of list to string in order 
# to apply join function to convert it into a string.
print(''.join(list(map(str, out))))











