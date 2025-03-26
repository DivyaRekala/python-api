import os
import psycopg2
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Database connection setup
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/api/data', methods=['GET','POST'])
def get_data():
    try:
        conn = get_db_connection()
        #cursor = conn.cursor()
        #cursor1 = conn.cursor()
        #cursor1.execute('SELECT * FROM my_table')  # Replace 'my_table' with your actual table name
        #cursor.execute('SELECT * FROM users')  # Replace 'users' with your actual table name
        #rows = cursor.fetchall()
        #rows1 = cursor1.fetchall()
        #return render_template('/app/app1.html', data=rows)
        conn.close()
   
        #data1 = [{"id": row[0], "name": row[1]} for row in rows1]
        #data = [{"id": row[0], "username": row[1], "password":row[2], "emailid":row[3], "mobile":row[4]} for row in rows]
        sample_data = [
    {"id": 1, "name": "Product A", "price": 29.99, "category": "Electronics"},
    {"id": 2, "name": "Product B", "price": 19.99, "category": "Books"},
    {"id": 3, "name": "Product C", "price": 49.99, "category": "Electronics"},
    {"id": 4, "name": "Product D", "price": 9.99, "category": "Toys"},
    {"id": 5, "name": "Product E", "price": 39.99, "category": "Clothing"}
]
        #return jsonify(data)
        return jsonify(sample_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return the error message in the response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
