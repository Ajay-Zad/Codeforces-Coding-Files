''' Author - Ajay Zad
    Date   - 15-03-2022 '''


n = int(input("Enter the size of the array :"))
l = []
for i in range(0,n):
    m = int(input("Enter the elements in the array (repeat the values) :"))
    l.append(m)
    
s = set(l)
l1 = list(s)
l1.sort()

for i in range(0,len(l1)):
    cnt = 0
    for j in range(0,n):
        if l1[i] == l[j]:
            cnt = cnt + 1
    print("Number ",l1[i]," is repeated for = ",cnt," times")
            

    
    