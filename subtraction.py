n , k = input().split()

for i in range(0,int(k)):
    rem = int(n) % 10
    if rem == 0:
        n = int(n) / 10
    else:
        n = int(n) - 1
        
print(int(n))
    