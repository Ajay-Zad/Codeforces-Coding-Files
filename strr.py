n = int(input())
for i in range(0,n):
    b = input()
    if(len(b)>10):
         print(b[0:1]+(str(len(b)-2))+b[(len(b)-1):len(b)])
         print()
    else:
        print(b)
        print()
    
    
    