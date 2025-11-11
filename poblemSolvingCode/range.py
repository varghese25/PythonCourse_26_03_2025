
#Loop vs List Comprehension

squares = []
for x in range (5):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(5)]
print(squares)