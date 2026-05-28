import requests
import sqlite3

URL = "https://dummyjson.com/products"

print("Fetching live data from supplier...")
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    products = data.get("products", [])

    print("Connecting to local database...")
    # 1. Connect to a database file named 'inventory.db'
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # 2. Create the table structure if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            stock INTEGER
        )
    """)

    # 3. Delete old data to prevent duplicates on multiple runs
    cursor.execute("DELETE FROM products")

    # 4. Loop through the live data and save each item into the database
    print("Saving data to SQLite...")
    for item in products:
        cursor.execute("""
            INSERT INTO products (id, name, price, stock)
            VALUES (?, ?, ?, ?)
        """, (item.get("id"), item.get("title"), item.get("price"), item.get("stock")))

    # 5. Lock in the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Success! {len(products)} products saved to 'inventory.db'.")

else:
    print(f"Failed to fetch data. Error: {response.status_code}")