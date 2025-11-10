import calendar



""" This script generates and prints the calendar for a specified year."""
year = 2025
month = 12 # December
date = 25

print(calendar.calendar(year)) # displays the full calendar for the year 2025
print(calendar.month(year, month)) # prints the calendar for December 2025


print('---------------------------------------------------------------------')


"""leap year check"""

year_arr = [2020, 2021, 2022, 2023, 2024]
for year in year_arr:
  print(year, calendar.isleap(year))

print('---------------------------------------------------------------------')


"""weekday check"""

print(calendar.weekday(2025, 12, 25)) # 3 means Thursday
# 0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday, 4: Friday, 5: Saturday, 6: Sunday