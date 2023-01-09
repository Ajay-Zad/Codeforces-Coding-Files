import math
s = input()
s1 = len(s)
a = 0
s4=''
s5=''
for i in s:
    if ord(i) >= 65 and ord(i) <= 90:
        a = a + 1

s2 = s1 - a
s3 = s1 / 2
if math.ceil(s3) > s2:
    s4 = s.upper()
    print(s4)
else:
    s5 = s.lower()
    print(s5)
