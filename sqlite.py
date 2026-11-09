import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

print("Database is ready!")

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS reviews (
#         id INTEGER PRIMARY KEY,
#         text TEXT,
#         label TEXT,
#         score INTEGER
#     )
# """)

# print("Table created!")

# cursor.execute(
#     "INSERT INTO reviews (text, label, score) VALUES (?, ?, ?)",
#     ("The biryani was amazing!", "positive", 5)
# )

# conn.commit()

# print("One review saved.")

# more_reviews = [
#     ("Delivery was very late and food was cold.", "negative", 1),
#     ("Good taste, fair price.", "positive", 4),
#     ("It was okay, nothing special.", "neutral", 3),
#     ("App kept crashing during payment.", "negative", 2),
# ]

# cursor.executemany(
#     "INSERT INTO reviews (text,label,score) VALUES (?,?,?)",
#     more_reviews
# )

# conn.commit()

# print("Added", len(more_reviews), "more reviews.")

# cursor.execute("SELECT * FROM reviews")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# cursor.execute("SELECT text, score FROM reviews WHERE label = ?", ("negative",))
# negatives = cursor.fetchall()

# print("Negative reviews: ")
# for text, score in negatives:
#     print("-", text, "(score:", score, ")")

# conn.close()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )
""")

print("Table created!")

productList = [
    ("Tea", 10),
    ("Fruits", 50),
    ("Biscuits",20),
    ("Milk",25),
    ("Paan",15)
]

# cursor.executemany("INSERT INTO product (name, price) VALUES (?, ?)",
#     productList
# )

# conn.commit()

# ================ delete data from a table ===============
# cursor.execute("DELETE FROM product WHERE id IN (6,7,8,9,10)")
# conn.commit()

cursor.execute("SELECT * FROM product")
rows = cursor.fetchall()

for row in rows:
    print(row)

print("==============================")
# ============ print all the tables ==============
cursor.execute("SELECT name FROM sqlite_schema WHERE type='table'")
rows = cursor.fetchall()

for row in rows:
    print(row)

# ====== DROP TABLE ============
# cursor.execute("DROP TABLE products")

conn.close()