import sys
s = input()
s1 = input()
s2 = input()
s4 = s + s1 
l = list(s4)
l1 = list(s2)
l.sort()
l1.sort()
for i in range(0,len(s2)):
    if len(s4) == len(s2):
        if l[i] == l1[i]:
            pass
        else:
            print("NO")
            sys.exit()
    else:
        print("NO")
        sys.exit()
        
print("YES")      