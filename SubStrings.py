t = int(input())
s1 = ''
for i in range(0,t):
    s = input()
    l1 = list(s)
    for j in range(2,len(l1)):
        if j % 2 == 0:
            pass
        else:
            s1 = s1 + l1[j]
            
    print(s[0:2]+s1)
    s1 = ''
            