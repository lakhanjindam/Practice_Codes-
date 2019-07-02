n = int(input())
s = set(map(int, input().split()))
cmd = int(input())

arr = []
for i in range(cmd):
    val = input().split(" ")
    if len(val)==1:
        s.pop()
    elif val[0] == "remove":
        s.remove(int(val[1]))
    elif val[0] == "discard":
        s.discard(int(val[1]))
    
        
    
print(sum(s))


