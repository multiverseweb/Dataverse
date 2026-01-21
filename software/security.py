import bcrypt
import secrets
import time
from typing import Optional, Dict
import db_config

class SecurityManager:
    """
    Comprehensive security manager for password hashing and session management
    """
    
    def __init__(self):
        self.active_sessions: Dict[str, Dict] = {}
        self.failed_attempts: Dict[str, Dict] = {}
        self.max_failed_attempts = 5
        self.lockout_duration = 900  # 15 minutes
    
    def hash_password(self, password: str) -> str:
        """
        Hash password using bcrypt with salt
        
        Args:
            password (str): Plain text password
            
        Returns:
            str: Hashed password
        """
        if not password:
            raise ValueError("Password cannot be empty")
            
        salt = bcrypt.gensalt(rounds=12)  # Higher rounds for better security
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """
        Verify password against hash
        
        Args:
            password (str): Plain text password
            hashed (str): Stored hash
            
        Returns:
            bool: True if password matches
        """
        try:
            if not password or not hashed:
                return False
            return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except Exception as e:
            print(f"Password verification error: {e}")
            return False
    
    def create_session(self, user_id: str, username: str) -> str:
        """
        Create secure session token
        
        Args:
            user_id (str): User ID
            username (str): Username
            
        Returns:
            str: Session token
        """
        token = secrets.token_urlsafe(32)
        current_time = time.time()
        
        self.active_sessions[token] = {
            'user_id': user_id,
            'username': username,
            'created_at': current_time,
            'last_activity': current_time,
            'ip_address': 'localhost'  # Can be extended for web version
        }
        
        # Clean up old sessions
        self._cleanup_expired_sessions()
        
        return token
    
    def validate_session(self, token: str) -> Optional[Dict]:
        """
        Validate session token and return session info if valid
        
        Args:
            token (str): Session token
            
        Returns:
            Optional[Dict]: Session info if valid, None otherwise
        """
        if not token or token not in self.active_sessions:
            return None
        
        session = self.active_sessions[token]
        current_time = time.time()
        
        # Check if session expired
        if current_time - session['last_activity'] > db_config.SESSION_TIMEOUT:
            del self.active_sessions[token]
            return None
        
        # Update last activity
        session['last_activity'] = current_time
        return session
    
    def destroy_session(self, token: str) -> bool:
        """
        Destroy session token
        
        Args:
            token (str): Session token
            
        Returns:
            bool: True if session was destroyed
        """
        if token in self.active_sessions:
            del self.active_sessions[token]
            return True
        return False
    
    def record_failed_attempt(self, username: str) -> bool:
        """
        Record failed login attempt and check if account should be locked
        
        Args:
            username (str): Username that failed login
            
        Returns:
            bool: True if account is now locked
        """
        current_time = time.time()
        
        if username not in self.failed_attempts:
            self.failed_attempts[username] = {
                'count': 0,
                'first_attempt': current_time,
                'locked_until': 0
            }
        
        attempt_info = self.failed_attempts[username]
        
        # Reset counter if it's been more than lockout duration since first attempt
        if current_time - attempt_info['first_attempt'] > self.lockout_duration:
            attempt_info['count'] = 0
            attempt_info['first_attempt'] = current_time
        
        attempt_info['count'] += 1
        
        # Lock account if too many failed attempts
        if attempt_info['count'] >= self.max_failed_attempts:
            attempt_info['locked_until'] = current_time + self.lockout_duration
            return True
        
        return False
    
    def is_account_locked(self, username: str) -> bool:
        """
        Check if account is currently locked
        
        Args:
            username (str): Username to check
            
        Returns:
            bool: True if account is locked
        """
        if username not in self.failed_attempts:
            return False
        
        attempt_info = self.failed_attempts[username]
        current_time = time.time()
        
        if attempt_info['locked_until'] > current_time:
            return True
        
        # Unlock account if lockout period has passed
        if attempt_info['locked_until'] > 0:
            attempt_info['count'] = 0
            attempt_info['locked_until'] = 0
        
        return False
    
    def clear_failed_attempts(self, username: str):
        """
        Clear failed attempts for successful login
        
        Args:
            username (str): Username to clear attempts for
        """
        if username in self.failed_attempts:
            del self.failed_attempts[username]
    
    def _cleanup_expired_sessions(self):
        """Clean up expired sessions"""
        current_time = time.time()
        expired_tokens = []
        
        for token, session in self.active_sessions.items():
            if current_time - session['last_activity'] > db_config.SESSION_TIMEOUT:
                expired_tokens.append(token)
        
        for token in expired_tokens:
            del self.active_sessions[token]
    
    def get_active_sessions_count(self) -> int:
        """Get count of active sessions"""
        self._cleanup_expired_sessions()
        return len(self.active_sessions)

# Global security manager instance
security_manager = SecurityManager()