a,b = input().split()
k = int(a)
k1 = int(b)
k2 = 0 
for i in range(0,10):
    k = k * 3
    k1 = k1 * 2
    k2+=1
    if k > k1 :
        break
print(k2)