# --- DEMO: Combining Nested Structures with Control Flow and Comprehensions ---

# Sample data: list of user dictionaries with a list of orders for each user
users_data = [
    {"user_id": 1, "name": "Alice", "orders": [{"order_id": "A1", "amount": 150}, {"order_id": "A2", "amount": 200}]},
    {"user_id": 2, "name": "Bob", "orders": [{"order_id": "B1", "amount": 50}]},
    {"user_id": 3, "name": "Charlie", "orders": []}
]

# Calculate the total amount spent by each user using a loop
print("Total amount spent by each user (using loop):")
for user in users_data:
    total_spent = 0
    for order in user.get("orders", []): # Use .get() for safe access
        total_spent += order.get("amount", 0) # Use .get() for safe access
    print(f"{user.get('name', 'N/A')}: ${total_spent}")

# Get a list of all order amounts across all users using a nested comprehension
all_order_amounts = [order.get("amount", 0) for user in users_data for order in user.get("orders", [])]
print("\nAll order amounts:", all_order_amounts)

# Create a dictionary mapping user_id to the number of orders using a dictionary comprehension
orders_count_by_user = {user.get("user_id"): len(user.get("orders", [])) for user in users_data}
print("Number of orders per user:", orders_count_by_user)