n = int(input())
s = input()
l = list(s)
one = l.count('1')
zero = l.count('0')
m = min(one,zero)
if m == one:
    print(zero-m)
else:
    print(one-m)


