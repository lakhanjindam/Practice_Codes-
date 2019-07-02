import re
c = int(input())
for i in range(0, c):
    try:
        re.compile(input().strip())
        print("True")

    except re.error:
        print("False")