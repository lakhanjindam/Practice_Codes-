def ducci_seq(l1):
    out= []
    
    for j in range(len(l1)):
        
        if j==len(l1)-1:
            out.append(l1[j]-l1[0])
        else:
            out.append(l1[j+1]-l1[j])
    
    return out


l1 = list(map(int, input().split()))
n = int(input())
for i in range(n+1):
    l1 = ducci_seq(l1)

print(l1)