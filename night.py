s = input()
x='a'
y=s[0]
sum1 = 0
for i in range(1,len(s)):
    b = abs(ord(x)-ord(y))
    sum1 = sum1 + min(b,26-b)
    x = y
    y = s[i]

b = abs(ord(x)-ord(y))
sum1 = sum1 + min(b,26-b)
print(sum1)