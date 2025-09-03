d  = {"p": 10, "q": 20}
print(d.pop("p"))

"""
The  pop () method removes the key  "P" from the dictionary and return its value, 10
 The dictionary becomes {"q":20}, but print() outPuts the return value 10.
"""


my_list = [10, 20, 30, 40]
removed_item = my_list.pop(1)  # Removes and returns 20
print(my_list)        # Output: [10, 30, 40]
print(removed_item)   # Output: 20
