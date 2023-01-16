import sys
n = int(input())
s = input()
s = s.upper()
l = list(s)
l.sort()
s1 = ''
for i in range(65,91):
    for j in l:
        if i == j:
            s = s + i
            
l1 = list(s)
set1 = set(l1)
l2 = list(set1)
l2.sort()
s2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l3 = list(s2)
s3=0
for i in range(0,len(l2)):
    if l2[i] == l3[i]:
        s3+=1
        pass
    else:
        print("NO")
        sys.exit()
        
if s3 == 26:
    print("YES")
else:
    print("NO")

            