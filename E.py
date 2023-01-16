def aa(a):
    f = a[0]
    l = a[len(a)-1]
    r = 1
    if f == 1 and l == 1:
        a.remove(f)
    elif f == 1 and l == 0:
        a.remove(f)
    elif f == 0 and l == 1:
        a.pop(len(a)-1)
    elif f == 0 and l == 0:
        a.remove(f)
        a.pop(len(a)-1)
        r = 2
        
        '''o = a.index(1)
        a.reverse()
        o1 = a.index(1)
        a.reverse()
        if o == o1:
            cnt2 = 0
            cnt3 = 0
            for i in range(o+1,len(a)):
                if a[i] == 1:
                    cnt2 = i
                    break
            a.reverse()
            for i in range(o1+1,len(a)):
                if a[i] == 1:
                    cnt3 = i
                    break
            a.reverse()
            if cnt2 >= cnt3:
                a.pop(len(a)-1)
            else:
                a.pop(0)
        elif o > o1:
            a.pop(len(a)-1)
        else:
            a.pop(0)'''
    else:
        pass
    return a,r
        
c = 0   
for _ in range(int(input())):
    n,s = input().split()
    n = int(n)
    s = int(s)
    x = [int(x) for x in input().split()]
    cnt = 0
    if sum(x) == s:
        print("0")
        continue
    elif sum(x) < s:
        print("-1")
        continue
    else:
        while sum(x) != s:
            x,r = aa(x)
            cnt = cnt + r
    print(cnt)