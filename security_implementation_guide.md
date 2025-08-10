# Security Implementation Guide for Dataverse

## Step 1: Update Requirements

First, add the new security dependencies to `installation/requirements.txt`:

```txt
bcrypt>=4.0.1
python-dotenv>=1.0.0
```

## Step 2: Create Environment Configuration

### Create `.env.example`:
```env
# Database Configuration
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_secure_password
DB_NAME=DATAVERSE

# Security Configuration
SECRET_KEY=your_secret_key_here
SESSION_TIMEOUT=3600
```

### Update `software/db_config.py`:
```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'DATAVERSE')
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
SESSION_TIMEOUT = int(os.getenv('SESSION_TIMEOUT', 3600))
```

## Step 3: Implement Secure Password Hashing

### Create `software/security.py`:
```python
import bcrypt
import secrets
import time
from typing import Optional, Dict

class SecurityManager:
    def __init__(self):
        self.active_sessions: Dict[str, Dict] = {}
    
    def hash_password(self, password: str) -> str:
        """Hash password using bcrypt with salt"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash"""
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except Exception:
            return False
    
    def create_session(self, user_id: str) -> str:
        """Create secure session token"""
        token = secrets.token_urlsafe(32)
        self.active_sessions[token] = {
            'user_id': user_id,
            'created_at': time.time(),
            'last_activity': time.time()
        }
        return token
    
    def validate_session(self, token: str) -> Optional[str]:
        """Validate session token and return user_id if valid"""
        if token not in self.active_sessions:
            return None
        
        session = self.active_sessions[token]
        current_time = time.time()
        
        # Check if session expired
        if current_time - session['last_activity'] > SESSION_TIMEOUT:
            del self.active_sessions[token]
            return None
        
        # Update last activity
        session['last_activity'] = current_time
        return session['user_id']
    
    def destroy_session(self, token: str) -> bool:
        """Destroy session token"""
        if token in self.active_sessions:
            del self.active_sessions[token]
            return True
        return False

# Global security manager instance
security_manager = SecurityManager()
```

## Step 4: Input Validation

### Create `software/validators.py`:
```python
import re
from typing import Optional

class InputValidator:
    @staticmethod
    def validate_username(username: str) -> bool:
        """Validate username format"""
        if not username or len(username) < 3 or len(username) > 50:
            return False
        # Allow alphanumeric and underscore only
        return re.match(r'^[a-zA-Z0-9_]+$', username) is not None
    
    @staticmethod
    def validate_password(password: str) -> bool:
        """Validate password strength"""
        if not password or len(password) < 8:
            return False
        # At least one uppercase, lowercase, digit
        has_upper = re.search(r'[A-Z]', password)
        has_lower = re.search(r'[a-z]', password)
        has_digit = re.search(r'\d', password)
        return all([has_upper, has_lower, has_digit])
    
    @staticmethod
    def validate_country(country: str) -> bool:
        """Validate country name"""
        if not country or len(country) > 100:
            return False
        # Allow letters, spaces, hyphens only
        return re.match(r'^[a-zA-Z\s\-]+$', country) is not None
    
    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """Basic input sanitization"""
        if not input_str:
            return ""
        # Remove potential SQL injection characters
        dangerous_chars = ["'", '"', ';', '--', '/*', '*/', 'xp_', 'sp_']
        sanitized = input_str
        for char in dangerous_chars:
            sanitized = sanitized.replace(char, '')
        return sanitized.strip()
```

## Step 5: Update Database Operations

### Update `software/manage_data.py`:
```python
import mysql.connector as my
from mysql.connector import Error
import db_config
from security import security_manager
from validators import InputValidator

# Secure database connection
def get_db_connection():
    try:
        connection = my.connect(
            host=db_config.DB_HOST,
            user=db_config.DB_USER,
            password=db_config.DB_PASSWORD,
            database=db_config.DB_NAME,
            autocommit=False  # Enable transactions
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None

def create_user_secure(username: str, password: str, country: str) -> tuple:
    """Securely create new user with proper validation"""
    validator = InputValidator()
    
    # Validate inputs
    if not validator.validate_username(username):
        return False, "Invalid username format"
    
    if not validator.validate_password(password):
        return False, "Password must be at least 8 characters with uppercase, lowercase, and digit"
    
    if not validator.validate_country(country):
        return False, "Invalid country format"
    
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if username already exists (parameterized query)
        check_query = "SELECT u_name FROM user WHERE u_name = %s"
        cursor.execute(check_query, (username,))
        
        if cursor.fetchone():
            return False, "Username already exists"
        
        # Hash password securely
        hashed_password = security_manager.hash_password(password)
        
        # Generate user ID
        import datetime
        u_id = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        
        # Insert user with parameterized query
        insert_query = """
            INSERT INTO user (u_id, u_name, pwd, country) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (u_id, username, hashed_password, country))
        
        connection.commit()
        return True, f"Account created successfully! User ID: {u_id}"
        
    except Error as e:
        connection.rollback()
        return False, f"Database error: {e}"
    finally:
        if connection:
            connection.close()

def authenticate_user_secure(username: str, password: str) -> tuple:
    """Securely authenticate user"""
    validator = InputValidator()
    
    if not validator.validate_username(username):
        return False, "Invalid username format", None
    
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed", None
    
    try:
        cursor = connection.cursor()
        
        # Get user data with parameterized query
        query = "SELECT u_id, pwd FROM user WHERE u_name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        if not result:
            return False, "User not found", None
        
        u_id, stored_hash = result
        
        # Verify password
        if security_manager.verify_password(password, stored_hash):
            # Create session token
            session_token = security_manager.create_session(str(u_id))
            return True, "Login successful", session_token
        else:
            return False, "Invalid password", None
            
    except Error as e:
        return False, f"Database error: {e}", None
    finally:
        if connection:
            connection.close()
```

## Step 6: Migration Script

### Create `migration_script.py`:
```python
"""
Migration script to update existing passwords to secure hashes
Run this ONCE after implementing the new security system
"""

import mysql.connector as my
from security import security_manager
import db_config

def migrate_passwords():
    """Migrate existing passwords to secure hashes"""
    connection = my.connect(
        host=db_config.DB_HOST,
        user=db_config.DB_USER,
        password=db_config.DB_PASSWORD,
        database=db_config.DB_NAME
    )
    
    cursor = connection.cursor()
    
    try:
        # Get all users with old password format
        cursor.execute("SELECT u_id, u_name, pwd FROM user")
        users = cursor.fetchall()
        
        for u_id, username, old_pwd in users:
            # Decrypt old password (using the old decrypt function)
            decrypted = decrypt_old_password(old_pwd)
            
            # Hash with new secure method
            new_hash = security_manager.hash_password(decrypted)
            
            # Update database
            update_query = "UPDATE user SET pwd = %s WHERE u_id = %s"
            cursor.execute(update_query, (new_hash, u_id))
            
            print(f"Migrated password for user: {username}")
        
        connection.commit()
        print("Password migration completed successfully!")
        
    except Exception as e:
        connection.rollback()
        print(f"Migration failed: {e}")
    finally:
        connection.close()

def decrypt_old_password(encrypted_password):
    """Decrypt password using old method (for migration only)"""
    password_length = len(encrypted_password)
    decrypted_password = ""
    if password_length % 2 == 0:
        transformed_pwd = encrypted_password[int(password_length / 2):]
        transformed_pwd += encrypted_password[:int(password_length / 2)]
    else:
        transformed_pwd = encrypted_password[int(password_length / 2) + 1:]
        transformed_pwd += encrypted_password[:int(password_length / 2) + 1]
    for character in transformed_pwd:
        decrypted_password += chr(ord(character) // 2)
    return decrypted_password

if __name__ == "__main__":
    migrate_passwords()
```

## Step 7: Update Main Application

### Update relevant functions in `software/main.py`:
```python
from security import security_manager
from validators import InputValidator
import manage_data

# Replace the old encrypt/decrypt functions with secure versions
def create_account_secure(username, password, country):
    """Secure account creation"""
    success, message = manage_data.create_user_secure(username, password, country)
    if success:
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", message)

def login_secure(username, password):
    """Secure login process"""
    success, message, session_token = manage_data.authenticate_user_secure(username, password)
    if success:
        # Store session token for the user session
        global current_session_token
        current_session_token = session_token
        messagebox.showinfo("Success", message)
        # Proceed to user menu
    else:
        messagebox.showerror("Error", message)
```

## Testing the Implementation

1. **Create `.env` file** with your database credentials
2. **Install new dependencies**: `pip install bcrypt python-dotenv`
3. **Run migration script** to update existing passwords
4. **Test user registration** with new validation
5. **Test login** with secure authentication
6. **Verify session management** works correctly

## Security Benefits

✅ **Strong Password Hashing**: bcrypt with salt prevents rainbow table attacks
✅ **Environment Variables**: No more hardcoded credentials
✅ **SQL Injection Prevention**: Parameterized queries eliminate injection risks
✅ **Input Validation**: Prevents malicious data entry
✅ **Session Management**: Secure token-based authentication
✅ **Backward Compatibility**: Migration script preserves existing users