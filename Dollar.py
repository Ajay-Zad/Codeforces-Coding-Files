n = int(input())
n1 = n // 100
r1 = n % 100
n2 = r1 // 20
r2 = r1 % 20
n3 = r2 // 10
r4 = r2 % 10
n5 = r4 // 5
r5 = r4 % 5
n6 = r5 // 1
print(n1+n2+n3+n5+n6)
    