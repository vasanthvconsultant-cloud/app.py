from flask import Flask
import pymysql
import os

app = Flask(__name__)

# Load RDS connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    return "Flask App Connected to RDS!"

@app.route("/users")
def users():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")  # Example table
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
