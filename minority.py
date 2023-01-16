t = int(input())
while t != 0:
    t = t - 1
    s = input()
    s1 = s.count('0')
    s2 = s.count('1')
    if len(s) == 1:
        print('0')
        continue
    elif s1 == s2:
        print(s1-1)
        continue
    else:
        pass
    s3 = min(s1,s2)
    print(s3)