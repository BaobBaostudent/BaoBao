# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:06:54 2024

@author: Student
"""

a = float(input("a = "));
b = float(input("b = "));
c = float(input("c = "));
if (a + b > c) and (b + c > a) and (a + c > b):
    print("3 cạnh là một tam giác");
else: 
    print("3 cạnh không phải là một tam giác")
    