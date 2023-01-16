t = int(input())
while t != 0 :
    t = t - 1
    t1 = input()
    t2 = input()
    l = []
    for i in t2:
        cnt = 0
        for j in range(0,len(t1)):
            if i == t1[j]:
                l.append(cnt+1)
                break
            else:
                cnt = cnt + 1
    sum1 = 0
    for i in range(1,len(l)):
        sum1 = sum1 + abs(l[i-1]-l[i])
    print(sum1)