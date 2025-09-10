d = {"x":5}
print(d.setdefault("y",10))

"""
The seldefault("y",10) method checks if key "y" exists in the dictionary d.
Since it doesn't, it adds "y":10 to the dictionary and returns the value 10.
"""