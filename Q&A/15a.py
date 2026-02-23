def gen():
    yield 1
    yield 2
    yield 3
g = gen()

print(list(g))
print(list(g))


""" Explanation:
Generators are exhausted after one iteration.
First list(g) consumes all values
Second call returns empty list because the generator has no more values to yield."""