# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:10:55 2022

@author: Ajay
"""


n = (input("Enter the number :"))

if n.isdigit():
    print("Digit")
elif n.isupper():
    print("Uppercase")
elif n.islower():
    print("Lowercase")
else:
    print("Special character")