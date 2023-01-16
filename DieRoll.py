from fractions import Fraction
y,w = input().split()
z = max(int(y),int(w))
a = (6-(int(z)-1))/6
b = (6-(int(z)-1))
if a == 1:
    print("1/1")
elif a == 0:
    print("0/1")
else:
    print(Fraction(b,6))