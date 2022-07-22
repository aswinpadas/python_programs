import datetime

month, day, year = (map(int, input().split()))
print(datetime.date(year, month, day).strftime("%A").upper())
