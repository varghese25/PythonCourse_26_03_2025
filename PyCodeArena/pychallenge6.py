# def deco(f):
#     def wrapper():
#         return f() + "!"
#     return wrapper
# @deco 
# def msg():
#     return "Hi"
# print(msg())




# Decorator Example
def logging(func):
        def wrapper():
          print(" Logging Started...")
          func()
          print(" Logging End..")
        return wrapper # returning the wrapper function
def add():
     print(10 + 20)
log = logging(add) # decorating the add function
log()  # calling the decorated function
    

    # log() calls the logging(fun) which returns the wrapper function 
    # again log() calls the wrapper function which prints the logging statements and calls the add function inside it.



# """Explanation:
# msg() calls the wrapper function and concatenates the result, so it prints Hi!

# Detailed Explanation:

# When you write @deco above msg(), it means:
# msg = deco(msg)

# So msg() no longer calls the original msg() function.
# Instead, it calls the wrapper() function that deco returns.

# Inside wrapper():
# return f() + "!"

# Here:

# f() → calls the original msg() → returns "Hi"

# "Hi" + "!" → gives "Hi!"

# So msg() prints Hi!


# """