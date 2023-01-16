for _ in range(int(input())):
    r,b,d = input().split()
    r = int(r)
    b = int(b)
    d = int(d)
    m = min(r,b)
    if m * (d+1) >= max(r,b):
        print("YES")
    else:
        print("NO")