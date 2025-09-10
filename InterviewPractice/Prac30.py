x = 1000
y = 1000
print(x is y)

"""
# False
# In Python, small integers (typically between -5 and 256) are cached and reused
# for memory efficiency. However, larger integers like 1000 are not cached,
# so x and y refer to different objects in memory, even though they have the same value.


"""