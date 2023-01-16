n1,m1 = input().split()
n = int(n1)
m = int(m1)
x = [int(x) for x in input().split()]
y = []
x.sort()
cnt = 0
for i in x:
    if i < 0:
        y.append(i)
        cnt = cnt  + 1
        if cnt == m:
            break
print(abs(sum(y)))

