if __name__ == '__main__':
    l1 = []
    N = int(input())
    for i in range(N):
        a = input().split(" ")
        command = a[0]
        if command == "insert":
            l1.insert(int(a[1]), int(a[2]))
        elif command == "append":
            l1.append(int(a[1]))
        elif command == "remove":
            l1.remove(int(a[1]))
        elif command == "print":
            print(list(map(int,l1)))
        elif command == "sort":
            l1.sort()
        elif command == "pop":
            l1.pop()
        elif command == "reverse":
            l1.reverse()
        
    

