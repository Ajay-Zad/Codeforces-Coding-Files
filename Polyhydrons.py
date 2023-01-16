n = int(input())
a = 0
for i in range(0,n):
    s = input()
    if s == 'Tetrahedron':
        a = a + 4
    elif s == 'Cube':
        a = a + 6
    elif s == 'Octahedron':
        a = a + 8
    elif s == 'Dodecahedron':
        a = a + 12 
    else:
        a = a + 20
        
print(a)
        