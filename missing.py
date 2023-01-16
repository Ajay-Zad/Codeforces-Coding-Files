''' Author - Ajay Zad
    Date   - 10/03/2022 '''
import sys    
n = int(input("Enter the value for n : "))
l = []
for i in range(1,n):
    n1 = int(input("Enter the value less than or equal to n without repeating the values :"))
    l.append(n1)
    
l.sort()
j = 1
for i in range(0,n-1):
    if j != l[i]:
        print("The missing number is ",j)
        sys.exit()
    j = j + 1
    
print("The missing number is ",n)
        