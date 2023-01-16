import sys
s = input()
s1 = set(s)
if len(s1) == 2:
    print("0")
    
if len(s1) > 3:
   print(len(s1)-4) 
   sys.exit()
else:
    print("1")
    sys.exit()
    
if len(s1) > 2:
    print(len(s1)-4)
    
else:
    print("0")