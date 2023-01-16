import sys
s = input()
n = int(input())
l = []
while n != 0 :
    n1 = input()
    l.append(n1)
    n = n - 1 


for i in l:
    if i == s:
        print("YES")
        sys.exit()
for i in l:
    for j in l:
        if s == (j[1:] + i[:1]):
            print("YES")
            sys.exit()
            
print("NO")
            
    
