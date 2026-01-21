import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'DATAVERSE')
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key-change-in-production')
SESSION_TIMEOUT = int(os.getenv('SESSION_TIMEOUT', 3600))
APP_DEBUG = os.getenv('APP_DEBUG', 'False').lower() == 'true'