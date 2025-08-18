data = {"a": 1, "b": 2}
print(data.get("c", 5) * data["a"])
# python Prac1.py , to run this code
"""
"c" does not exist in data.

If we used data["c"], Python would crash with a KeyError.

Using data.get("c", 5) safely returns 5, so the program runs correctly.

So the comment is basically saying:
👉 “To safely fetch values from a dictionary, especially when the key might not exist, use dict.get().”
"""
