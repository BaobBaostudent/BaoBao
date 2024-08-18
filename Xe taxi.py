# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:59:57 2024

@author: ADMIN
"""

a = float(input("Tiền taxi theo số (km)"));
if a  <= 1:
    st=20
    print("Số tiền phải trả", st);
elif  a <= 3:
    st=a*13
    print("Số tiền phải trả", st);
elif a <= 4 and a <= 8:
    st=3*13+(a-3)*12
    print("Số tiền phải trả", st);
elif a > 8:
    st=3*13+ 5*12+ (a-8)*10
    print("Số tiền phải trả", st);
if st > 100:
    stc = st*0.92
    print("Số tiền cuối cùng phải trả", stc)