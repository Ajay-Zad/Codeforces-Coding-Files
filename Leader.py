digits = [8]
digits.reverse()
cnt = 0
if len(digits) == 1:
    digits[0] = digits[0] + 1
for i in range(1,len(digits)):
    if cnt == 0:
        cnt = 1
        digits[i-1] = digits[i-1] + 1
    if digits[i-1] > 9:
        digits[i-1] = 0
        digits[i] = digits[i] + 1
e = digits[len(digits)-1] 
c = e
if e > 9:
    temp = e % 10
    digits.append(temp)
    e = e // 10
    digits.append(e)
    if c in digits:
        digits.remove(c)
digits.reverse()
print(digits)
        