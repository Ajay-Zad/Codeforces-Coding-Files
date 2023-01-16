''' Name - Ajay Zad 
    Date - 14/03/2022 '''

n = int(input("Enter the value for n :"))
cnt = 0 
print("The Prime numbers are :")
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            cnt = cnt + 1
        
    if cnt == 0:
        print(i)
    cnt = 0