n = int(input())
k=0
for i in range(0,n):
    a , b , c = input().split()
    if(int(a) == 1 and int(b) == 1 and int(c) == 1):
        k = k + 1
    elif(int(a) == 0 and int(b) == 1 and int(c) == 1):
        k = k + 1
    elif(int(a) == 1 and int(b) == 0 and int(c) == 1):
        k = k + 1
    elif(int(a) == 1 and int(b) == 1 and int(c) == 0):
        k = k + 1
    else:
        pass
print(k)
        

        
