n1 = 1000000
prime = [1 for i in range(n1+1)]
p = 2
while p * p <= n1:
    if prime[p] == 1:
        for i in range(p*2,n1+1,p):
            prime[i] = 0
    p+=1
    
l = []
for i in range(2,n1):
     if prime[i]:
         l.append(i*i)

    
n = int(input())
x = [int(x) for x in input().split()]
for i in range(0,n):
    if x[i] in l:
        print("YES")
    else:
        print("NO")