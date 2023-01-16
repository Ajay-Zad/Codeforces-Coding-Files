s1,s2,s3,s4 = input().split()
l = []
l.append(s1)
l.append(s2)
l.append(s3)
l.append(s4)

s = set(l)

if len(s) == 1:
    print("3")
elif len(s) == 2:
    print("2")
elif len(s) == 3:
    print("1")
else:
    print("0")