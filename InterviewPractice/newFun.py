x = 'awesome' # # Global variable
def myfunc():
 x = 'fantastic' #  # Local variable (only inside myfunc)
print('Python is ' + x) # Function runs, but doesn’t change the global x
myfunc()

"""
Above code if i want to print Gloabl dont indent

If i want to print local indent the print statement inside the function
"""