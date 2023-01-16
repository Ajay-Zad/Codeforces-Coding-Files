n = int(input())
a = [int(a) for a in input().split()]
s = []
d = []
i = 0 
j = len(a) - 1
t = 0
while i <= j :
    if t == 0:
        if a[i] > a[j]:
            s.append(a[i])
            i = i + 1
        else:
            s.append(a[j])
            j = j - 1
        t = 1
    else:
        if a[i] > a[j]:
            d.append(a[i])
            i = i + 1
        else:
            d.append(a[j])
            j = j - 1
        t = 0

print(sum(s),sum(d))
            
    