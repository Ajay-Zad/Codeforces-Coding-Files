s1 = input()
n = int(s1)
if n > 0:
    print(n)
else:
    b = s1[len(s1)-1]
    a = s1[len(s1)-2]
    s2 = s1[0:len(s1)-2]
    aa = s2+a
    bb = s2+b
    n1 = int(aa)
    n2 = int(bb)
    if n1 >= n2:
        print(n1)
    else:
        print(n2)
