int(input())
x = [int(x) for x in input().split()]
cnt = 0
for i in range(1,len(x)-1):
    if x[i-1] == 1 and x[i] == 0 and x[i+1] == 1:
        cnt = cnt + 1
        x[i+1] = 0
print(cnt)
        
