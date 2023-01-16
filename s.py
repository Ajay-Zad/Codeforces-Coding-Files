import math
for _ in range(int(input())):
    n = int(input())
    n1 = round(n/3)
    n2 = math.ceil(n/3)
    if n1 == n2:
        n3 = math.floor(n/3)
        s1=s2= n1
        if s1 == s2:
            s1 = s1 + 1
            n3 = n3 - 1
        if s2 == n3:
            s1 = s1 + 1
            n3 = n3 - 1
    else:
        n3 = math.ceil(n/3)
        s1 = s2 = n1
        if s1 == s2:
            s1 = s1 + 1
            n3 = n3 - 1
        if s2 == n3:
            s1 = s1 + 1
            n3 = n3 - 1
    print(s2,s1,n3)
        
   