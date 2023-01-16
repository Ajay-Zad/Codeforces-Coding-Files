t = int(input())
s = input()
s1 = set()
l = []
for i in range(1,len(s)):
    s1.add(s[i-1]+s[i])
    l.append(s[i-1]+s[i])
cnt = 0
s2 = ""
for i in s1:
    cnt1 = l.count(i)
    if cnt1 > cnt :
        cnt = cnt1
        s2 = i
print(s2)