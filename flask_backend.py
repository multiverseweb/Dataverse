from flask import Flask, render_template, session, redirect, url_for, request
import mysql.connector

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="finance_data"
    )

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Fetch user's visualizations
    cursor.execute("SELECT * FROM visualizations WHERE user_id = %s", (user_id,))
    visualizations = cursor.fetchall()

    # Fetch user's uploaded data
    cursor.execute("SELECT * FROM uploaded_data WHERE user_id = %s", (user_id,))
    uploaded_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('dashboard.html', visualizations=visualizations, uploaded_data=uploaded_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check credentials (add hash check for security)
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            session['user_id'] = user['user_id']
            return redirect(url_for('dashboard'))

        return "Invalid credentials", 401

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
