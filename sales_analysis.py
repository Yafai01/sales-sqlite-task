import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# 2. Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# 3. Insert sample data
data = [
    ("Laptop", 5, 50000),
    ("Phone", 10, 20000),
    ("Tablet", 7, 15000),
    ("Laptop", 3, 50000),
    ("Phone", 5, 20000)
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", data)
conn.commit()

# 4. SQL query
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# 5. Load result into pandas
df = pd.read_sql_query(query, conn)

# 6. Print output
print(df)

# 7. Plot bar chart
df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()
