import sys
s = input()
l = list(s)
a = 0 
s1 = ''
s2 = ''
b = 0 
s3 = ''
if ord(l[0]) >= 97 and ord(l[0]) <= 122 and len(s) == 1:
    s3 = s.upper()
    print(s3)
    sys.exit()
    
if ord(l[0]) >= 65 and ord(l[0]) <= 90 and len(s) == 1:
    s3 = s.lower()
    print(s3)
    sys.exit()
    
for i in range(0,len(s)):
    if ord(l[i]) >= 65 and ord(l[i]) <= 90:
        a+=1
        
    if a == len(s):
        s1 = s.lower()
        print(s1)
        sys.exit() 
i = 1
while ord(l[0]) >= 97 and ord(l[0]) <= 122:
    if ord(l[i]) >= 65 and ord(l[i]) <= 90:
        s2 = s.capitalize()
        if i == len(s)-1:
            b = 1
            break
    else:
        print(s)
        sys.exit()
    i+=1
if b == 1:
    print(s2)   
    sys.exit()

j = 1
while ord(l[0]) >= 65 and ord(l[0]) <= 90:
    if ord(l[j]) >= 97 and ord(l[j]) <= 122:
        print(s)
        sys.exit()
    else:
        print(s)
        sys.exit()

    
        
    