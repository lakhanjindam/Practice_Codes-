N = int(input())
l1= []
for i in range(N):
    l1.append(list(map(int,input().split())))
max_list = []
max1 = 0
max2 = 0 
max3 = 0 
for i in range(len(l1)):
    
    if len(l1)==1:
        max_list.append(l1[i])
        print(max_list)
    else:
        for j in range(len(l1[i])):
            if max1 < l1[i][j]:
                max1 = l1[i][j]
            elif  max2 < l1[i][j+1]:
                max2 = l1[i][j+1]
                j = j-1
            elif max3 < l1[i][j+2]:
                max3 = l1[i][j+2]
                j = j-2

max_list.append(max1)
max_list.append(max2)
max_list.append(max3)
print(max_list)
            




