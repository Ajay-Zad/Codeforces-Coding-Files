input()
s = input()
s2 = ""
l=[]
if len(s) == s.count('x'):
    print(len(s)-2)
else:
    for i in s:
        if i == 'x':
            s2 = s2 + i
        else:
            l.append(s2)
            s2 = ""
    l.append(s2)
    s1 = 0
    for i in l:
        if len(i) == 3:
            s1 = s1 + 1
        if len(i) > 3:
            s1 = s1 + (len(i)-2)
    print(s1)
    