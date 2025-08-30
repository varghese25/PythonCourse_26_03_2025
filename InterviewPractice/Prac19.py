L1 = [1,2,3,4,5]
L2 = []  # Empty list

for n in L1:
    if n == 2:
     L1.remove(2)

    L2.append(n)

print(L2)

"""
Explanation:
The code iterates over the list L1 and removes the element 2 from it while simultaneously appending each element to the new list L2. However, modifying a list while iterating over it can lead to unexpected behavior. In this case, when 2 is removed, the subsequent elements shift left, causing the loop to skip the next element (which is 3). As a result, L2 ends up being [1, 3, 4, 5] instead of [1, 2, 3, 4, 5].


"""
