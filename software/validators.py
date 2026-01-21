import re
from typing import Optional, List

class InputValidator:
    """
    Comprehensive input validation and sanitization utilities
    """
    
    # SQL injection patterns to detect
    SQL_INJECTION_PATTERNS = [
        r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|EXEC|UNION|SCRIPT)\b)",
        r"(--|#|/\*|\*/)",
        r"(\b(OR|AND)\s+\d+\s*=\s*\d+)",
        r"(\bOR\s+\w+\s*=\s*\w+)",
        r"(\';|\"\;)",
        r"(\bxp_|\bsp_)"
    ]
    
    @staticmethod
    def validate_username(username: str) -> tuple[bool, str]:
        """
        Validate username format and security
        
        Args:
            username (str): Username to validate
            
        Returns:
            tuple[bool, str]: (is_valid, error_message)
        """
        if not username:
            return False, "Username cannot be empty"
        
        if len(username) < 3:
            return False, "Username must be at least 3 characters long"
        
        if len(username) > 50:
            return False, "Username cannot exceed 50 characters"
        
        # Allow alphanumeric, underscore, and hyphen only
        if not re.match(r'^[a-zA-Z0-9_-]+$', username):
            return False, "Username can only contain letters, numbers, underscore, and hyphen"
        
        # Check for SQL injection patterns
        if InputValidator._contains_sql_injection(username):
            return False, "Username contains invalid characters"
        
        # Username cannot start with number
        if username[0].isdigit():
            return False, "Username cannot start with a number"
        
        return True, ""
    
    @staticmethod
    def validate_password(password: str) -> tuple[bool, str]:
        """
        Validate password strength and security
        
        Args:
            password (str): Password to validate
            
        Returns:
            tuple[bool, str]: (is_valid, error_message)
        """
        if not password:
            return False, "Password cannot be empty"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        if len(password) > 128:
            return False, "Password cannot exceed 128 characters"
        
        # Check for required character types
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        missing_requirements = []
        if not has_upper:
            missing_requirements.append("uppercase letter")
        if not has_lower:
            missing_requirements.append("lowercase letter")
        if not has_digit:
            missing_requirements.append("digit")
        if not has_special:
            missing_requirements.append("special character")
        
        if missing_requirements:
            return False, f"Password must contain at least one: {', '.join(missing_requirements)}"
        
        # Check for common weak patterns
        if InputValidator._is_weak_password(password):
            return False, "Password is too common or weak"
        
        return True, ""
    
    @staticmethod
    def validate_country(country: str) -> tuple[bool, str]:
        """
        Validate country name format
        
        Args:
            country (str): Country name to validate
            
        Returns:
            tuple[bool, str]: (is_valid, error_message)
        """
        if not country:
            return False, "Country cannot be empty"
        
        if len(country) > 100:
            return False, "Country name cannot exceed 100 characters"
        
        # Allow letters, spaces, hyphens, and apostrophes only
        if not re.match(r"^[a-zA-Z\s\-']+$", country):
            return False, "Country name contains invalid characters"
        
        # Check for SQL injection
        if InputValidator._contains_sql_injection(country):
            return False, "Country name contains invalid characters"
        
        return True, ""
    
    @staticmethod
    def validate_numeric_input(value: str, field_name: str, min_val: float = None, max_val: float = None) -> tuple[bool, str]:
        """
        Validate numeric input for financial data
        
        Args:
            value (str): Value to validate
            field_name (str): Name of the field for error messages
            min_val (float, optional): Minimum allowed value
            max_val (float, optional): Maximum allowed value
            
        Returns:
            tuple[bool, str]: (is_valid, error_message)
        """
        if not value:
            return False, f"{field_name} cannot be empty"
        
        try:
            num_value = float(value)
        except ValueError:
            return False, f"{field_name} must be a valid number"
        
        if min_val is not None and num_value < min_val:
            return False, f"{field_name} cannot be less than {min_val}"
        
        if max_val is not None and num_value > max_val:
            return False, f"{field_name} cannot exceed {max_val}"
        
        # Check for reasonable financial values (not more than 1 trillion)
        if abs(num_value) > 1_000_000_000_000:
            return False, f"{field_name} value is unreasonably large"
        
        return True, ""
    
    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """
        Basic input sanitization
        
        Args:
            input_str (str): Input string to sanitize
            
        Returns:
            str: Sanitized string
        """
        if not input_str:
            return ""
        
        # Remove potential dangerous characters
        sanitized = input_str.strip()
        
        # Remove null bytes
        sanitized = sanitized.replace('\x00', '')
        
        # Remove control characters except newline and tab
        sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\n\t')
        
        return sanitized
    
    @staticmethod
    def _contains_sql_injection(input_str: str) -> bool:
        """
        Check if input contains potential SQL injection patterns
        
        Args:
            input_str (str): String to check
            
        Returns:
            bool: True if potential SQL injection detected
        """
        input_upper = input_str.upper()
        
        for pattern in InputValidator.SQL_INJECTION_PATTERNS:
            if re.search(pattern, input_upper, re.IGNORECASE):
                return True
        
        return False
    
    @staticmethod
    def _is_weak_password(password: str) -> bool:
        """
        Check if password is commonly used or weak
        
        Args:
            password (str): Password to check
            
        Returns:
            bool: True if password is weak
        """
        # Common weak passwords
        weak_passwords = {
            'password', '12345678', 'qwerty123', 'abc123456', 
            'password123', '123456789', 'welcome123', 'admin123',
            'letmein123', 'monkey123', 'dragon123', 'master123'
        }
        
        if password.lower() in weak_passwords:
            return True
        
        # Check for keyboard patterns
        keyboard_patterns = ['qwerty', 'asdfgh', 'zxcvbn', '123456', '654321']
        password_lower = password.lower()
        
        for pattern in keyboard_patterns:
            if pattern in password_lower:
                return True
        
        # Check for repeated characters (more than 3 in a row)
        if re.search(r'(.)\1{3,}', password):
            return True
        
        return False
    
    @staticmethod
    def validate_session_token(token: str) -> bool:
        """
        Validate session token format
        
        Args:
            token (str): Session token to validate
            
        Returns:
            bool: True if token format is valid
        """
        if not token:
            return False
        
        # Session tokens should be URL-safe base64 strings of specific length
        if not re.match(r'^[A-Za-z0-9_-]{43}$', token):
            return False
        
        return True