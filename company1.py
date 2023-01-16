import sys
n = int(input())
a = []
for i in range(0,n):
    b = int(input())
    a.append(b)

a.sort()
i = 0 
while i < n:
    if i+1 >= n:
        print(a[n-1])
        sys.exit()
        
    if a[i] == a[i+1]:
        i = i + 2
    else:
        break
print(a[i])