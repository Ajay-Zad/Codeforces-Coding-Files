t = int(input())
while t != 0:
    t = t - 1
    s = input()
    s1 = input()
    
    if s[0] == s1 or s[len(s)-1] == s1:
        print("YES")
    elif s1 in s: 
        for i in range(0,len(s)):
            if s[i] == s1:
                if i % 2 == 0:
                    print("YES")
                    break
        if i == len(s)-1:
            print("NO")
            continue
    else:
        print("NO")
