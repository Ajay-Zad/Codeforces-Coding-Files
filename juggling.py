for _ in range(int(input())):
    n = int(input())
    l=[]
    for i in range(0,n):
        s1 = input()
        l.append(s1)
    l1 = []
    for i in l:
        for j in i:
            l1.append(j)
    s = set(l1)
    l2 = []
    for i in s:
        cnt = l1.count(i)
        l2.append(cnt)
    for i in l2:
        if i % n != 0:
           print("NO")
           break
    else:
        print("YES")