

def call (f, n):
    for _ in range(n):
        f() # Function if None is not callable, it will raise a TypeError.

        # correct way to call the function
        #f('hi')

call(print('hi'), 3)

# Python evaluates arguments before calling the function.

# Correct way call 
# call(print, 3)
'''Explanation:
The following code raises a TypeError
because we called "print()" directly when included it as an 
argument. This means the first thing we see in the console is: "hi
". Since the print function returns "none" as a result, Python then tries to call "none"in the for-loop, which doesn't
work because the NoneType is not callable.'''
