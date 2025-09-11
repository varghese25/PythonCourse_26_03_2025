# Unique Visitors Counter (Set usage)
# Dataset Example:
def count_unique_visitors(visitors):
    count = len(set(visitors))
    unique = set(visitors)
    return count, unique
visitors = ["A123", "B456", "A123", "C789", "B456", "D000"]
unique, count = count_unique_visitors(visitors)
# Task: count_unique_visitors(visitors) → return count of unique visitors.
print("count", count)
print("unique", unique)