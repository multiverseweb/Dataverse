import tkinter as tk
from tkinter import messagebox
import unittest
import sqlite3

# Database connection function
def connect_to_db():
    try:
        conn = sqlite3.connect('database.sql')
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
        return None

# Function to check credentials
def check_credentials(username, password):
    if not username or not password:
        messagebox.showerror("Invalid Input", "Username and password cannot be empty")
        return False

    conn = connect_to_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()
        if result:
            return True
        else:
            messagebox.showerror("Invalid Credentials", "Username or password is incorrect")
            return False
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to check credentials: {e}")
        return False

# Function to fetch data
def fetch_data(u_id):
    if not isinstance(u_id, int) or u_id <= 0:
        messagebox.showerror("Invalid Input", "User ID must be a positive integer")
        return None

    conn = connect_to_db()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data WHERE u_id=?", (u_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result
        else:
            messagebox.showerror("No Data Found", "No data found for the given user ID")
            return None
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to fetch data: {e}")
        return None

# Function to decrypt data
def decrypt(data):
    if not data or len(data) % 2 != 0:
        messagebox.showerror("Invalid Input", "Data must be a non-empty string with even length")
        return None

    # Decrypt logic here
    return data

class TestErrorHandling(unittest.TestCase):

    def test_check_credentials_valid_input(self):
        self.assertTrue(check_credentials("test_user", "test_password"))

    def test_check_credentials_invalid_input(self):
        self.assertFalse(check_credentials("", "test_password"))
        self.assertFalse(check_credentials("test_user", ""))
        self.assertFalse(check_credentials("", ""))

    def test_fetch_data_valid_input(self):
        self.assertIsNotNone(fetch_data(1))

    def test_fetch_data_invalid_input(self):
        self.assertIsNone(fetch_data(0))
        self.assertIsNone(fetch_data(-1))
        self.assertIsNone(fetch_data("test"))

    def test_decrypt_valid_input(self):
        self.assertIsNotNone(decrypt("test_data"))

    def test_decrypt_invalid_input(self):
        self.assertIsNone(decrypt(""))
        self.assertIsNone(decrypt("test"))

if __name__ == "__main__":
    unittest.main()