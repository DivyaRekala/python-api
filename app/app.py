import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Database connection setup
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_table')  # Replace 'my_table' with your actual table name
        rows = cursor.fetchall()
        conn.close()

        data = [{"id": row[0], "name": row[1]} for row in rows]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return the error message in the response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
