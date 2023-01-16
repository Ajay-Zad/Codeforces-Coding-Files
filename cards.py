import sys
s = input()
a,b,c,d,e = input().split()
for i in s:
    if i in a or i in b or i in c or i in c or i in d or i in e:
        print("YES")
        sys.exit()
        
print("NO")