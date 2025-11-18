def generator():
    for i in range(3):
      yield i
g = generator()
print(next(g))

"""
A.0
B. 012
c. 0123
d. None"""