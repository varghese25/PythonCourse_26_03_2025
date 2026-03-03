def gen():
    yield from [1,2,3]
g = gen()

print(next(g))
print(next(g))
print(list(g))

# yield from yields items sequentially. Two Values consumed -> remainig [3]