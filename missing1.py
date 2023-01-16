# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:03:38 2022

@author: Ajay
"""


n = int(input("Enter the value for n : "))
l = []
sum = 0
for i in range(1,n):
    n1 = int(input("Enter the value less than or equal to n without repeating the values :"))
    l.append(n1)
    sum = sum + n1
    
sum1 = 0    
for i in range(1,n+1):
    sum1 = sum1 + i
    
print("The missing number is ",(sum1-sum))
    