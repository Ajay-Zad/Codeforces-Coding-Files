''' Author - Ajay Zad
    date   - 08/03/2022 '''
# n defines number of lines     
n = int(input("Enter for n :"))
stars = 1
spaces = n     
for i in range(0,n):
    #loop for implementing spaces
    for j in range(spaces,0,-1):
        print(" ",end="")
    
    #loop for printing stars
    for k in range(0,stars):
        print("*",end="")
    print()
    stars = stars + 2
    spaces = spaces - 1
    
stars = (n*2) - 1
spaces = 1
for i in range(0,n):
    for j in range(0,spaces):
        print(" ",end="")
    
    for k in range(stars,0,-1):
        print("*",end="")
    print()
    stars = stars - 2
    spaces = spaces + 1