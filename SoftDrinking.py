n, k, l, c, d, p, nl, np = input().split()
print(min((int(k) * int(l))//int(nl),int(c)*int(d),int(p)//int(np))//int(n))