"""
Email Configuration for YOLO Object Detection
This module contains email settings and SMTP configuration for sending notifications.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Email Configuration for Password Reset
# Update these settings for production use

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USE_TLS = True

# Email credentials (use environment variables in production)
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')  # Your Gmail address
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Your Gmail App Password (16 characters)

# Email settings
FROM_EMAIL = os.getenv('FROM_EMAIL', EMAIL_USERNAME)  # Should match your Gmail address
FROM_NAME = os.getenv('FROM_NAME', 'YOLO Object Detection')

# Email templates
PASSWORD_RESET_SUBJECT = os.getenv(
    'PASSWORD_RESET_SUBJECT',
    'Password Reset Request - YOLO Object Detection'
)

def get_password_reset_body(username, reset_url):
    """Generate password reset email body"""
    return f"""Hello {username},

You have requested to reset your password for your YOLO Object Detection account.

Click the following link to reset your password:
{reset_url}

This link will expire in 1 hour.

If you did not request this password reset, please ignore this email.

Best regards,
{FROM_NAME}
"""

# Instructions for setting up Gmail SMTP:
# 1. Enable 2-factor authentication on your Gmail account
# 2. Generate an App Password: https://myaccount.google.com/apppasswords
# 3. Use the App Password instead of your regular password
# 4. Update EMAIL_USERNAME and EMAIL_PASSWORD above
# 5. App Password should be 16 characters long (e.g., "abcd efgh ijkl mnop")

# For production, use environment variables:
# import os
# EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
# EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
