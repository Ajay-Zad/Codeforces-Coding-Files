import math
for _ in range(int(input())):
    s = int(input())
    if s == 1:
        print(s)
        continue
    s1 = len(str(s))
    x = 10**(s1-1)
    s1 = s
    while 0 < s:
        s = s - x
        s = s + round(x/10)
        s1 = s1 + round(x/10)
    print(s1-1)