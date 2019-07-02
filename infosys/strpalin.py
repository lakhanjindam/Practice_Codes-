#PF-Assgn-57
def check_prime(number):
    #remove pass and write your logic here. if the number is prime return true, else return false
    if number > 1:

        for i in range(2, number):
            if(number%i==0):
                return False
            else:
                return True


def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

    i=1
    out = []
    while i<4:
        a = num[1:]+num[:1]
        out.append(a)
        i+=1 


def get_circular_prime_count(limit):
    pass #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))