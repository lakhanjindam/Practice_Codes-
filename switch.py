def one():
    return "one"

def two():
    return "two"

def switch(arguments):

    switcher = {
        0:one,
        1:two
        
    }

    print(switcher.get(arguments, lambda :"incorrect function"))

a = input()
switch(a)