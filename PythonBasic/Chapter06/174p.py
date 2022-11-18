import datetime
from datetime import date, time

today = date(2022, 11, 17)

print(today)
'''
print(today.year)
print(today.month)
print(today.day)
'''

print()

day = ['월','화','수','목','금','토','일']
w = day[today.weekday()]

print(f'오늘은 {today} {w}요일 입니다')
