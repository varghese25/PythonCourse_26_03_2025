
# Above code if i want to print Gloabl dont indent

x = 'awesome' # # Global variable
def myfunc():
 x = 'fantastic' #  # Local variable (only inside myfunc)
print('Python is ' + x) # Function runs, but doesn’t change the global x
myfunc()



# If i want to print local indent the print statement inside the function
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)





# # Insert the correct keyword to make the variable x belong to the global scope.
# def myfunc():
#   global x # Use the global keyword
#   x = "fantastic"