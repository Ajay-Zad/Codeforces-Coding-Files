t = int(input())
i = 0 
while i < t :
    i = i + 1
    a = int(input())
    if 360 % (180 - a) == 0:
        print("YES")
    else:
        print("NO")