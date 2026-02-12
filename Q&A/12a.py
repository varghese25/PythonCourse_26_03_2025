a = [1,2,3]
b = a
b = b + [4]
print(a)
print(b)

"""b=b+[4] creates a new list a still points to the original list"""



""" Just a small correction: (4) is an int. Adding a comma (4,) makes it a tuple, which allows tuple concatenation."""
a = (1,2,3)
b = a
b = b + (4,)
print(a)
print(b)

# OutPut
# print(a) -> (1, 2, 3)
# print(b) ->(1, 2, 3, 4)

# NB: b + (4) Python sees it as tuple + int
# Tuples can only be concatenated with other tuples, not integers. 