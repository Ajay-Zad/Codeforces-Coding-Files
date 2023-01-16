n1,m1 = input().split()
n = int(n1)
m = int(m1)
l = []
for i in range(2,100):
    cnt = 0
    for j in range(2,i+1):
        if i % j == 0:
            cnt = cnt + 1
    if cnt == 1:
        l.append(i)
        
f = l.index(n)
if m == l[f+1]:
    print("YES")
else:
    print("NO")
    
            