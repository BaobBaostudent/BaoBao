# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:01:18 2024

@author: Student
"""

nguoichoi=float(input("Người chọn (1.kéo,2.búa,3.bao): "))
from random import randint
maychon=randint(1,3)
if maychon==1:
    print("Máy chọn: Kéo")
elif maychon==2:
    print("Máy chọn: Búa")
elif maychon==3:
    print("Máy chọn: Bao")
if maychon==nguoichoi:
    print("Kết quả hòa")
elif (maychon ==1 and nguoichoi ==2) or (maychon ==2 and nguoichoi ==3) or (maychon ==3 and nguoichoi ==1):
    print ("Bạn thắng")
else:
    print ("Máy thắng")