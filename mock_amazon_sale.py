import sqlite3
import random

print("Listening for live Amazon orders...\n")

# 1. Connect to your central data warehouse
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# 2. Check what items we actually have in stock to sell
cursor.execute("SELECT id, name, stock, price FROM products WHERE stock > 0")
available_items = cursor.fetchall()

if not available_items:
    print("Warehouse is empty! Nothing to sell.")
else:
    # 3. Simulate a random customer clicking "Buy Now"
    sold_item = random.choice(available_items)
    item_id = sold_item[0]
    item_name = sold_item[1]
    current_stock = sold_item[2]
    price = sold_item[3]

    new_stock = current_stock - 1

    # 4. THE CORE BUSINESS LOGIC: Update the database instantly
    cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, item_id))
    conn.commit()

    print(f"💰 CHA-CHING! Customer bought: {item_name}")
    print(f"💵 Revenue: ${price}")
    print(f"📦 Stock updated: {current_stock} -> {new_stock}")

conn.close()