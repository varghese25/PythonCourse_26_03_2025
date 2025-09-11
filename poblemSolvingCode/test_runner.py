customers = [ "John Doe john@example.com", "Jane Smith jane.smith@work.org", "Foo Bar foo@bar.net" ]
email = [customer.split()[-1] for customer in customers]
print(email)

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