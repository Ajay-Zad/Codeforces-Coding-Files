n = int(input())
s = 'I hate'
s1 = 'I love'
s3 =''
for i in range(1,n+1):
    if i % 2 == 1:
        s3 = s3 + s
        s3 = s3 + ' that '
    
    if i % 2 == 0:
        s3 = s3 + s1
        s3 = s3 + ' that '
        
s4 = s3[0:len(s3)-5]
print(s4+"it")
        
    