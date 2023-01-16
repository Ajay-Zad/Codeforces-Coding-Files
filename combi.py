n = int(input())
s1 = (input())
s2 = (input())
sum1 = 0
for i,j in zip(s1,s2):
    s3 = min(abs(int(i)-int(j)),(10-(abs(int(i)-int(j)))))
    sum1 = sum1 + s3
print(sum1)