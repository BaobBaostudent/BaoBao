# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:06:13 2024

@author: Student
"""


DTB = float(input("Nhập điểm trung bình (GPA)"));
if DTB < 3.5:
    print("Học lực kém");
elif DTB <= 3.5 and DTB < 5.0:
    print("Học lực yếu");
elif DTB <= 5.0 and DTB < 7.0:
    print("Học lực trung bình");
elif DTB <= 7.0 and DTB < 8.0:
    print("Học lực khá");
elif DTB <= 8.0 and DTB < 9.0:
    print("Học lực giỏi");
elif DTB <= 9.0 and DTB <= 10:
    print("Học lực xuất sắc")