from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'dataverse'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    # Fetch reviews from the database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM reviews ORDER BY timestamp DESC')
    reviews = cursor.fetchall()
    conn.close()

    return render_template('index.html', reviews=reviews)

@app.route('/submit-review', methods=['POST'])
def submit_review():
    data = request.get_json()

    name = data['name']
    email = data['email']
    rating = int(data['rating'])
    review_text = data['review']
    timestamp = datetime.now()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO reviews (name, email, rating, review, timestamp) VALUES (%s, %s, %s, %s, %s)',
        (name, email, rating, review_text, timestamp)
    )
    conn.commit()
    conn.close()

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
