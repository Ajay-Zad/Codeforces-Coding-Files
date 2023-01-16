n = int(input())
x = [int(x) for x in input().split()]
s = 0
cnt = 0
for i in range(1,len(x)):
    if x[i-1] < x[i]:
        cnt = cnt + 1
    else:
        s = max(s,cnt+1)
        cnt = 0
s=max(cnt+1,s)
        
print(s)