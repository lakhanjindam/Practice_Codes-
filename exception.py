c = int(input())

for i in range(0, c):
    
    try:
        a,b = map(int, input().split(" "))
        #floor division to round off the value
        print(a//b)

    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as eb:
        print("Error code:", eb)