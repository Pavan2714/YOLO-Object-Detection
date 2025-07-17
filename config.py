"""
Configuration settings for YOLOv11 application.
Loads environment variables and provides app-wide constants.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Holds configuration variables for database, authentication, and app settings.
    """

    # Database configuration
    DB_PATH = os.getenv('DB_PATH')
    DB_CONFIG = {
        'database': DB_PATH
    }

    # Secret key for session management and token generation
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Admin credentials
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

    # Google OAuth configuration
    GOOGLE_CLIENT_ID = os.getenv(
        'GOOGLE_CLIENT_ID'
    )
    GOOGLE_CLIENT_SECRET = os.getenv(
        'GOOGLE_CLIENT_SECRET'
    )
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid_configuration"

    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    PORT = int(os.getenv('PORT', '4000'))  # Default should be a string

    # Application specific folders and allowed extensions
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    RESULT_FOLDER = os.getenv('RESULT_FOLDER')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'mp4'}
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
