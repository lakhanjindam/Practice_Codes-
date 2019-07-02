def swap_case(s):

    s = list(s)
    string = []
    for i in (s):
        if(i.isupper()):
            string.append(i.lower())
        else:
            string.append(i.upper())
    
    return (''.join(string))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)