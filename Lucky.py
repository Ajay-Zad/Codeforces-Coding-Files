n = int(input())
l = [4,7,74,47,44,77,444,474,747,777,477,447,774,744]

for i in l :
    if n == i or n % i == 0:
        print("YES")
        break
else:
    print("NO")
        
        
    