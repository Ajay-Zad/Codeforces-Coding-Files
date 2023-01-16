n, k = input().split()
n1 = int(n)
k1 = int(k)
c = 240 - k1
sum1 = 0
a=0
for i in range(1,n1+1):
    sum1 = sum1 + (5*i)
    if sum1 <= c:
        a+=1
    else:
        break
    
print(a)
        
    
