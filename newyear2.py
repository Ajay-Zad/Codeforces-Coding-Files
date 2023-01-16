x1,x2,x3 = input().split()
x11 = int(x1)
x22 = int(x2)
x33 = int(x3)
l = [x11,x22,x33]
l.sort()
x44 = min(x11,x22,x33)
x55 = max(x11,x22,x33)

x66 = x55 - l[1]
x77 = l[1] - x44
print(x66+x77)