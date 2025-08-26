a=[1,2,3,6,3,4,5]*2
b=max(set(a),key=a.count)
print(b)

"""
Step 1: Create list a
means the list is repeated twice.
a = [1, 2, 3, 6, 3, 4, 5, 1, 2, 3, 6, 3, 4, 5]

Step 2: Convert to a set
set(a) = {1, 2, 3, 4, 5, 6}

Step 3: Find element with max(..., key=a.count)
Here, Python checks each element in {1,2,3,4,5,6}
and applies a.count(x) → counts how many times it appears in list a.

a.count(1) = 2

a.count(2) = 2

a.count(3) = 4 ✅ (highest)

a.count(4) = 2

a.count(5) = 2

a.count(6) = 2


Step 4: Return the max

The element with the maximum count is 3.

print(b)  # 3

Output: 3


"""