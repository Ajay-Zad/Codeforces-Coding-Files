t =  int(input())
while t != 0:
    t = t - 1
    h1,m1 = input().split()
    h = int(h1)
    m = int(m1)
    to = 24 * 60
    to = to - h * 60
    to = to - m
    print(to)