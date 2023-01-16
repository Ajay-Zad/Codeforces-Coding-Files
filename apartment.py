k = int(input())
x = [int(x) for x in input().split()]
x.sort(reverse=True)
sum1 = 0 
cnt = 0
for i in x:
    if sum1 <= k:
        if sum1 == k:
            break
        sum1 = sum1 + i
        cnt = cnt + 1

if sum(x) < k:
    print("-1")
else:
    print(cnt)
    
        
