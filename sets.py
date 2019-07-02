m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

diff1  = sorted(a.difference(b))
list1 = set()
for i in diff1:
    print(list1.add(i)
