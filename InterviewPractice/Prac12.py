numbers=[10,35,50,60,75] # A list of 5 numbers
num=numbers[::2]  # Slice operation with step 2
print(num)

# Explanation
# The slice operation [::2] selects every second element from the list, starting from index 0.
# numbers[::2] means:
# Start from the beginning (: → no start index).
# Go until the end (: → no end index).
# Take every 2nd element (2 = step).


# Calculation
"""
Original list: [10, 35, 50, 60, 75]

Take index 0 → 10

Skip index 1 → 35

Take index 2 → 50

Skip index 3 → 60

Take index 4 → 75
"""