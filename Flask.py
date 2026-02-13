from flask import Flask
import pymysql
import os

app = Flask(__name__)

# Database configuration (Replace with your values)
DB_HOST = "your-rds-endpoint"
DB_USER = "admin"
DB_PASSWORD = "Admin123"
DB_NAME = "testdb"
DB_PORT = 3306


def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/")
def home():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW() as current_time;")
            result = cursor.fetchone()
        connection.close()

        return f"Database Time: {result['current_time']}"

    except Exception as e:
        return f"Database connection failed: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
