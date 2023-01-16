s = input()
s6 = ''
s6 = s6+s
l = list(s)
s1 = ''
s2 = ''
s3 = ''
s4 = ''
s5 = ''
a = 0
b = 0
c = 0
for i in range(0,len(s)):
    while ord(l[i]) >= 65 and ord(l[i]) <= 90:
        c+=1
        i+=1
        if i == 1:
            break
        if i == len(s)-1:
            break
        
    if c == 1:
        print(s6)
        break
    
    while ord(l[i]) >= 97 and ord(l[i]) <= 122:
        s1 = s1+l[i]
        s1 = s1.upper()
        s2 = s2+s[1:len(s)]
        s3 = s2.lower()
        s4 = s1+s3
        print(s4)
        a+=1
        break
    if a == 1:
        break

    
    while ord(l[i]) >= 65 and ord(l[i]) <= 90:
        b+=1
        if b == 2:
            s5 = s.lower()
            print(s5)
            break
    if b == 2:
        break
    
    