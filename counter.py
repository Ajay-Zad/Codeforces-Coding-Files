# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:48:32 2022

@author: Ajay
"""
import sys
l = []
n = int(input("Enter the size of array :"))
for i in range(0,n):
    m = int(input("enter the elements in the array :"))
    l.append(m)

cnt = 0
j = 0
i = 0
cnt1 = 0
while i < n:
    while l[j] >= 0:
        l[j] = l[j] - 1
        cnt = cnt+1
    else:
        try:
            cnt1 = cnt1 + 1
            l[j] = l[cnt]
        except:
            print(cnt1)  
            sys.exit()
    n = n - cnt
    
print(cnt1)

   
   
        
    











