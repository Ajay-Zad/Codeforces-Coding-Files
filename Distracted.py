t = int(input())
while 0 < t :
    n = int(input())
    s = input()
    a = set()
    i = 1
    while i < len(s):
        if s[i-1] != s[i]:
            a.add(s[i-1])
            if s[i] in a:
                print("NO")
                break
        i = i + 1
    if s[i-1] not in a:
        print("YES")
    t = t - 1
    
                