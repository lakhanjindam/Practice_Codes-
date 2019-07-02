def print_formatted(number):
    binary = bin(number)[2:]
    octal = oct(number)[2:]
    hexa = hex(number)[2:]
    print("{0}   {1}   {2}   {3}".format(number,octal,hexa.upper(),binary))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)