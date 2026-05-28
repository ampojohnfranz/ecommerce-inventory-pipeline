import sqlite3

print("Connecting to the data warehouse...")

# 1. Connect to the database we created in Step 1
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# 2. Write the SQL Query (The exact business logic)
# This translates to: "Give me the name, stock, and price of items with less than 10 units, sorted from lowest stock to highest."
sql_query = """
    SELECT name, stock, price
    FROM products
    WHERE stock < 10
    ORDER BY stock ASC
"""

# 3. Execute the query and fetch the results
cursor.execute(sql_query)
low_stock_items = cursor.fetchall()

# 4. Print the cleaned, actionable data for the business
print("\n--- ACTION REQUIRED: LOW STOCK ALERT ---")
for item in low_stock_items:
    name = item[0]
    stock = item[1]
    price = item[2]
    print(f"ORDER MORE: {name} | Only {stock} left | Unit Price: ${price}")

# Close the connection
conn.close()