n = int(input())
x = [int(x) for x in input().split()]
l=[]
for i in range(1,len(x)):
    diff = x[i-1] - x[i]
    l.append(abs(diff))
    
m = min(l)
j=0
for i in l:
    if i == m:
        j = j + 1
        break
    j = j + 1

diff = x[0] - x[len(x)-1]
if abs(diff) < m:
    print("1",len(x))
else:
    print(j,j+1)

