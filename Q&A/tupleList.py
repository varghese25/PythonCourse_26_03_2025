


# tuple & list behavior ()tuple , [] list


a = ([1]), ([2])
b = a
b[0].append(11)
b +=([3], )
b[1].append(22)
b[2].append(33)
print(a)

'''
a is a tuple of lists -> ([1], [2])
b = a -> both point to the same tuple
append() modifies the list inside the tuple (allowed)
+= creates a new tuple, so b separates from a 
Shared lists still reflect changes

Note: Tuples are immutable, but mutable objects inside them can still change.'''