n1 = (input())
n2 = (input())
s3 = ''
for i in range(0,len(n1)):
    if n1[i] == n2[i]:
        s3 = s3 + '0'
    else:
        s3 = s3 + '1'

print(s3)