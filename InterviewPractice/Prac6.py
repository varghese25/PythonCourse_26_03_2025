class Name:
    def __init__(self, name) -> None: 
        self.name = name
a = Name('Bob')
b = Name('Bob')
  
print(a == b)  
print(a is b)  

"""

Step 1: a == b

By default, classes in Python don’t define how equality (==) should work.

So a == b will behave like a is b unless you define an __eq__ method.

In this case, since __eq__ is not defined, a == b will be False (not True).

🔎 Step 2: a is b

is checks whether both variables refer to the same object in memory.

a and b are two different objects (Name('Bob') created twice).

So a is b is False.
"""