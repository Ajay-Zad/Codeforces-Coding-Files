l=[[0 for j in range(5)]for i in range(10)]
for i in range(0,10):
    for j in range(0,5):
        l[i][j] = i*j
        
print(l)