# Customer Email Extractor (List + String Processing)
# Dataset Example:

import email

from lark import Visitor


customers = [ "John Doe john@example.com", "Jane Smith jane.smith@work.org", "Foo Bar foo@bar.net" ]
email = [customer.split()[-1] for customer in customers]
print(email)

# Task: extract_emails(customers) → return list of emails only.
