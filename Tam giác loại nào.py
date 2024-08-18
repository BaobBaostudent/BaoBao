# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:19:17 2024

@author: Student
"""

a = float(input("a ="));
b = float(input("b ="));
c = float(input("c ="));
if (a + b > c) and (b + c > a) and (a + c > a): 
    if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == b*b + a*a):
        print("Tam giác vuông");
    elif (a == b) and (b == c):
        print("Tam giác đều");
    elif (a*a > b*b+c*c) or (b*b > a*a+c*c) or (c*c > a*a+b*b): 
        print("Tam giác tù");
    else:
        print("Tam giác nhọn");
else:
    print("Không phải 3 cạnh của một tam giác")
        

