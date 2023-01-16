n , k = input().split()
b = 0
c = [int(x) for x in input().split()]
for i in c:
    if i >= c[int(k)-1] and i > 0  :
        b = b + 1
              
print(b)