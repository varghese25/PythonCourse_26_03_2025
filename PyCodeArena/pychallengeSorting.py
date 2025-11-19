
#Question:Sort the list in ascending order and remove duplicates.

numbers = [5, 2, 9, 1, 5, 6]

# Expected output: [1, 2,5,6,9]

unique_sorted = sorted(set(numbers))
print(unique_sorted)

''''Explanation:  
- set() removes duplicates  
- sorted() arranges the list in order'''