| Structure  | Symbol | Meaning            |
| ---------- | ------ | ------------------ |
| Dictionary | `:`    | mapping / relation |
| Set        | `,`    | collection         |
| List       | `[]`   | ordered items      |
| Tuple      | `()`   | fixed items        |

# One sentence to remember forever <br>

- If you are pairing things → use :<br>
- If you are grouping things → use ,<br>

# Meaning of def **init**

\*\* -- def → means define a function.

\*\* **init** → means initialize (short form of initializer).

-- Exmple constructor.py

# What are the three main types of methods in a Python class ?

--1> Instance Methods - work with object data using self.
--2> Class Methods - work with class-level data using cls.
--3> Static Methods - general utility methods, not tied to class or instance data.

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

# self

Can you use another name instead of self?

✅ Yes, absolutely — self is just a naming convention, not a keyword.

Python, developers always use self for readability and consistency.
self -> Refers to the current instance of the class
