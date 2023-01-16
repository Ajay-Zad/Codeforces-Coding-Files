for _ in range(int(input())):
    a,b,n,s = input().split()
    a = int(a)
    b = int(b)
    n = int(n)
    s = int(s)
    if s % n <= b and ((a*n)+b) >= s:
        print("YES")
    else:
        print("NO")