from threading import Thread #from threading module import Thread function 

def tryit1():
    name=input("Enter your name")
    print("Hi your name is ",name)

def tryit2():
    for i in range(1,10):
        x=i*2.0
    print("Done")


# to initialize a thread
thread1 = Thread(target = tryit1)

#starts the execution of thread
thread1.start()

thread2 = Thread(target=tryit2)   #we are creating one thread for tryit2
thread2.start()     #we are starting that thread

#we are waiting for the threads to complete using join.
thread1.join()
thread2.join()


#2
#PF-Tryout

def func1():
    result_sum=0
    #Write the code to find the sum of numbers from 1 to 10000000
    
    for i in range(1,1000000):
        result_sum+=i
        
    print("Sum from func1:",result_sum)

def func2():
    result_sum=0
    #Write the code to accept 5 numbers from user and find its sum
    a = list(map(int, input().split(" ")))
    for i in a:
        result_sum+=i

    print("Sum from func2:",result_sum)

#Modify the code given below to execute func1() and func2() in two separate threads
thread11 = Thread(target = func1)
thread11.start()

thread12 = Thread(target = func2)
thread12.start()

thread11.join()
thread12.join()
