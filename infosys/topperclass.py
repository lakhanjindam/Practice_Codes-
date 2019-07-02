n = ["George:96:78:89","Ruby:85:87:98"]
details = []
for i in range(len(n)):
    details.append(n[i].split(":"))

print(details)
marks = []
for i in range(len(details)):
    marks.append(details[i][-3:])

print(marks)
sci = []
maths = []
eng = []
for i in range(len(marks)):
    sci.append(marks[i][:1])
    maths.append(marks[i][2:2])
    eng.append(marks[i][-1:])

print(sci, maths, eng)