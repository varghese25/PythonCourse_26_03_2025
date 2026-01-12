# a = 5
# b = '3'
# print(a*b)


# """
# Number * Number -> mathematical multiplication
# Number * String -> string repetition
# String * Number -> string repetition
# String * String -> Error
# String + String -> string concatenation
# String + Number -> Error"""


x = 0
for i in range(3):
    x = x + i
print(x)




# | Iteration | i | x before | x = x + i | x after |
# | --------- | - | -------- | --------- | ------- |
# | 1         | 0 | 0        | 0 + 0     | 0       |
# | 2         | 1 | 0        | 0 + 1     | 1       |
# | 3         | 2 | 1        | 1 + 2     | 3       |

"""
Explanation:

The output of this code depends on the indentation of print(x), because indentation defines code blocks in Python.

1) If print(x) is outside the for loop, it executes after the loop completes, and the final value of x will be 3.
2) If print(x) is inside the loop, it executes on every iteration, and the outputs will be 0, 1, and 3.
3) If indentation is incorrect or inconsistent, the code will result in an 
IndentationError."""