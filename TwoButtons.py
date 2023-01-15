n2, m1 = input().split()
n = int(n2)
m = int(m1)

if n % 2 == 0:
    n1 = n // 2
    print(n1)
else:
    n = n + 1
    n1 = n // 2
    print(n1)