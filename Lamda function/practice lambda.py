#1. Filtering Out Inactive Users
#Scenario: You have a list of user dictionaries, and you want to quickly filter out the users
#who are currently inactive.
users = [{"username": "Alice","Active": "True"},
         {"username":"Bob", "Active":"False"},
         {"username":"Charlie", "Active":"True"}]
# Using lambda with filter()
active_users = list(filter(lambda user: user["active"], users))

print(active_users)
# Output: [{'username': 'alice', 'active': True}, {'username': 'charlie', 'active': True}]
2. Sorting a List of Products by Price
Scenario: You are building an e-commerce sorting feature and need to sort a list of products from cheapest to most expensive.
Python
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 25.50},
    {"name": "Keyboard", "price": 75.00}
]

# Using lambda as the sorting key
sorted_products = sorted(products, key=lambda p: p["price"])

print(sorted_products)
# Output: [{'name': 'Mouse', 'price': 25.5}, {'name': 'Keyboard', 'price': 75.0}, {'name': 'Laptop', 'price': 999.99}]
3. Applying a Discount to Prices
Scenario: A flash sale requires applying a 20% discount across an entire list of item prices.
Python
prices = [100, 250, 50, 500]

# Using lambda with map() to apply a 20% discount (multiply by 0.8)
discounted_prices = list(map(lambda price: price * 0.8, prices))

print(discounted_prices)
# Output: [80.0, 200.0, 40.0, 400.0]


1. Extracting Specific Data from API Responses
Scenario: An API returns a list of user profiles, but your UI only needs a list of their email addresses.
Python
profiles = [
    {"id": 1, "email": "alice@example.com"},
    {"id": 2, "email": "bob@example.com"},
    {"id": 3, "email": "charlie@example.com"}
]

# Using lambda with map() to extract just the emails
emails = list(map(lambda profile: profile["email"], profiles))

print(emails)
# Output: ['alice@example.com', 'bob@example.com', 'charlie@example.com']
2. Finding the Longest Word in a List
Scenario: You want to find the longest search keyword entered by users from a list of strings.
Python
keywords = ["python", "lambda", "programming", "code"]

# Using max() with a lambda key to find the longest string by length
longest_keyword = max(keywords, key=lambda word: len(word))

print(longest_keyword)
# Output: programming
3. Conditional Formatting / Quick Inline Logic
Scenario: You are generating a receipt summary and need a quick inline check to see if an order qualifies for free shipping (orders over $50).
Python
# A lambda with a conditional (ternary) expression inside
shipping_status = lambda amount: "Free Shipping" if amount > 50 else "Standard Shipping ($5)"

print(shipping_status(35))
# Output: Standard Shipping ($5)

print(shipping_status(75))
# Output: Free Shipping
4. Cleaning Up String Input (Stripping Whitespace)
Scenario: Users typed extra spaces around their usernames in a form, and you want to clean them up instantly.
Python
raw_inputs = ["  alice ", "bob   ", "  charlie  ", "diana"]

# Using lambda with map() to strip whitespace from each string
cleaned_inputs = list(map(lambda name: name.strip(), raw_inputs))

print(cleaned_inputs)
# Output: ['alice', 'bob', 'charlie', 'diana']

Scenario: An API returns a list of user profiles, but your UI only needs a list of their email addresses.
Python
profiles = [
    {"id": 1, "email": "alice@example.com"},
    {"id": 2, "email": "bob@example.com"},
    {"id": 3, "email": "charlie@example.com"}
]

# Using lambda with map() to extract just the emails
emails = list(map(lambda profile: profile["email"], profiles))

print(emails)
# Output: ['alice@example.com', 'bob@example.com', 'charlie@example.com']
2. Finding the Longest Word in a List
Scenario: You want to find the longest search keyword entered by users from a list of strings.
Python
keywords = ["python", "lambda", "programming", "code"]

# Using max() with a lambda key to find the longest string by length
longest_keyword = max(keywords, key=lambda word: len(word))

print(longest_keyword)
# Output: programming
3. Conditional Formatting / Quick Inline Logic
Scenario: You are generating a receipt summary and need a quick inline check to see if an order qualifies for free shipping (orders over $50).
Python
# A lambda with a conditional (ternary) expression inside
shipping_status = lambda amount: "Free Shipping" if amount > 50 else "Standard Shipping ($5)"

print(shipping_status(35))
# Output: Standard Shipping ($5)

print(shipping_status(75))
# Output: Free Shipping
4. Cleaning Up String Input (Stripping Whitespace)
Scenario: Users typed extra spaces around their usernames in a form, and you want to clean them up instantly.
Python
raw_inputs = ["  alice ", "bob   ", "  charlie  ", "diana"]

# Using lambda with map() to strip whitespace from each string
cleaned_inputs = list(map(lambda name: name.strip(), raw_inputs))

print(cleaned_inputs)
# Output: ['alice', 'bob', 'charlie', 'diana']


