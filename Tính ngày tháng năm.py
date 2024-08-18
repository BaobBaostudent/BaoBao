# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:00:00 2024

@author: ADMIN
"""

def is_leap_year(year):
    """Kiểm tra xem năm có phải là năm nhuận không."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def validate_date(day, month, year):
    """Kiểm tra tính hợp lệ của ngày tháng năm."""
   
    if year < 1 or month < 1 or month > 12:
        return "Không hợp lệ"
    
    
    days_in_month = {
        1: 31, 2: 29 if is_leap_year(year) else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if day < 1 or day > days_in_month.get(month, 0):
        return "Không hợp lệ"
    
    return f"Ngày {day:02d}/{month:02d}/{year} là ngày hợp lệ."


print("Kiểm tra tính hợp lệ của ngày tháng năm")
year = int(input("Nhập năm: "))
month = int(input("Nhập tháng: "))
day = int(input("Nhập ngày: "))


result = validate_date(day, month, year)
print(result)