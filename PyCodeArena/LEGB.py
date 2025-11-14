# """
# L - Local (inside the current function)

# E - Enclosing (in the outer function, if functions are nested)

# G - Global (module-level variables)

# B - Built-in (Python’s built-in names like len, print, etc.)

# """
# # Python is an interpreted language
# """Python code is not compiled ahead of time (like Java .class files).
# The Python interpreter reads the code top-to-bottom, 
# line by line.Each line is executed immediately, except for things like function or class definitions, 
# which only create objects but don't run the body yet."""




# # Execution flow rules
# # Top-level statements
# #Python runs them immediately in the order they appear.

# #Example:1

# print("Line 1")
# x = 5
# print("Line 2:", x)

# print("======================================================================")

# # Examople:2

# # Function and class definitions
# # def or class statements create objects (functions/classes) but do not execute the body yet.
# # Body executes only when the function is called or the class is instantiated.



# def greet():
#     print("Hello, Team!")

# print("Before calling") # First this line will be printed

# greet() # Then the function is called, and "Hello, Team!" is printed

# print("After calling") # Finally, this line will be printed



print("======================================================================")

# Example:3
# Nested functions
# Inner functions are defined only when the outer function runs.


def outer():
    print("Hi From outer function!")
    
    def inner():
        print("Hello from inner function!")
    
    inner()  # inner() is called inside outer()

outer()  # only need to call outer, if comment this line no output will be there 

# Step-by-step explanation

# def outer(): ...

# Python creates the function object outer.

# The body of outer does not run yet.

# outer() is commented out

# So the body of outer never executes.

# This means:

# "Hi From outer function!" is never printed

# The nested function inner() is never defined or called, so "Hello from inner function!" is also never printed

# Result: no output in the console.