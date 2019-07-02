from itertools import permutations

s,a= input().split()
result = (permutations(sorted(s),int(a)))

for i in (result):
    print(''.join(i))
    
