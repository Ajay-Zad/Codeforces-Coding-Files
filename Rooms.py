n = int(input())
a = 0

for i in range(0,n):
    p,q = input().split()
    r = int(q) - int(p)
    if r >= 2:
        a+=1
    
print(a)