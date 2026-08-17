print("Script started")

from sqlalchemy import text
from database.db_connection import engine

print("Imports successful")

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM retail_sales"))
        print("✅ Connected Successfully!")
        print("Rows:", result.scalar())
except Exception as e:
    print("❌ Connection Failed")
    print(e)