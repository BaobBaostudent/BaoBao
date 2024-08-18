# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:44:21 2024

@author: Student
"""
import math;
a = float(input("a = "));
b = float(input("b = "));
c = float(input("c = "));
delta = b * b - 4 * a * c
if delta >  0:
    x1 = float((-b + math.sqrt(delta)) / (2 * a))
    x2 = float((-b - math.sqrt(delta)) / (2 * a))
    print("Phương trình có hai nghiệm phân biệt là: ");
elif delta == 0:
    x = -b / ( 2 * a)
    print("Phương trình có nghiệm kép là: ");
else: 
    print("Phương trình vô nghiệm")