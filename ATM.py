x1,y1 = input().split()
x = int(x1)
y = int(y1)
if x % 5 == 0:
    if y >= x :
        z = y - (x+0.5)
        print(float(z))
    else:
        print(float(y))
else:
    print(float(y))
