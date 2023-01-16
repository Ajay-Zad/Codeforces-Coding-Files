n1,k1 = input().split()
n = int(n1)
k = int(k1)
x = [int(x) for x in input().split()]
cnt = 0
for i in range(0,n):
    if 5 - x[i] >= k:
        cnt += 1
ans = cnt / 3
print(int(ans))  
