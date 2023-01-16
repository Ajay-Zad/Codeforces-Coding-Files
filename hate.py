for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        print("0")
        continue
    if s[len(s)-1] == '1' and s[0] == '0':
        l = list(s[1:len(s)-2])
        if sum(l) == 0:
            print("0")
        else:
            print(sum(l))
    elif s[len(s)-1] == '0' and s[0] == '1':
         l = list(s[1:len(s)-2])
         if sum(l) == 0:
             print("0")
         else:
             print(sum(l))
    elif s[len(s)-1] == '0' and s[0] == '0':
        l = list(s[1:len(s)-2])
        if s == '010':
            print("1")
            continue
        print(l)
        print(sum(l))
    else:
        l = list(s[1:len(s)-2])
        print(sum(l)+1)
        
             