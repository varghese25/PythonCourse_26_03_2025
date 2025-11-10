# Run Jupyter (without worrying about PATH)

After installation, instead of jupyter notebook, run:

# To Start

C:\Users\u>python -m notebook

# To Stop

Ctrl+C

In Python, the -m flag means:
👉 “Run a module as a script.”

This directly tells Python to launch Jupyter, so you don’t need PATH set up yet.

👉 If it works, your browser will open at:

http://localhost:8888/tree

# Python Data Structures Comparison: List vs Tuple vs Set

| Feature    | List (`[]`) | Tuple (`()`) | Set (`{}`) |
| ---------- | ----------- | ------------ | ---------- |
| Duplicates | YES         | YES          | NO         |
| Ordered    | YES         | YES          | NO         |
| Mutable    | YES         | NO           | YES        |

Sept 02 2025

sepators code (-)

# import calendar

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
