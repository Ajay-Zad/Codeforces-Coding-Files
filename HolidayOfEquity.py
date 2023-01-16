n = int(input())
x = [int(x) for x in input().split()]
y = max(x)
s = 0
for i in range(0,len(x)):
    s1 = y - x[i]
    s = s + s1
    
print(s)
    