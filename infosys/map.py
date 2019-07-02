'''def upper(letter):
    if letter.isupper():
        return letter.lower()
    else:
        return letter.upper()

a = input()
print(''.join(map(upper, a)))
'''
a = ["lakhan", "jindam"]
i = 0
b = []
for each in a:
    b.append(a[i].upper())
    i+=1

c = ' '.join(b)
print(c)