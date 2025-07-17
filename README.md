# YOLOv11 Flask Web App

A modern Flask web application for object detection using YOLOv11, supporting both manual and Google OAuth login, user dashboard, password reset, and more.

## Features

- Manual username/password signup & login
- Google OAuth login/signup
- Secure password reset via email
- User dashboard with image/video uploads and detection results
- Profile image support (Google or local upload)
- Admin dashboard
- Responsive, modern UI
- SQLite database (with migration support)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/YOLOv11.git
cd YOLOv11
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

- Copy `env_example.txt` to `.env` and fill in your secrets (Flask secret key, Google client ID/secret, etc.)

### 4. Google OAuth Setup

- Create a Google Cloud project and OAuth 2.0 credentials
- Set the client ID/secret in your `.env` or `config.py`
- Add your authorized redirect URI (e.g., `http://localhost:4002/google-callback`)

### 5. Email/Password Reset Setup

- Enable 2-factor authentication on your Gmail account
- Generate a Gmail App Password: https://myaccount.google.com/apppasswords
- Set your Gmail address and App Password in `email_config.py`

### 6. Run the App

```bash
python3 webapp.py
```

Visit [http://localhost:4002](http://localhost:4002) in your browser.

## Usage

- **Sign up** with username/password or Google
- **Login** and access your dashboard
- **Upload images/videos** for detection
- **Forgot password?** Use the reset link (check your email or console)
- **Admin**: Use `/admin/login-new` for admin dashboard

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Files/Folders to Exclude from GitHub

Add the following to your `.gitignore` to avoid uploading sensitive or unnecessary files:

```
# Model weights
*.pt

# Database
*.db
yolov11.db

# User uploads/results
uploads/
static/uploads/
static/results/

# Output files
output.mp4
runs/

# Cache and temp files
__pycache__/
*.pyc
*.pyo
*.cache

# Environment/config
.env
.env.*

# System files
.DS_Store
Thumbs.db

# Logs
*.log

# IDE/project files
.vscode/
.idea/
```

**Do NOT upload your Google credentials, App Password, or any private keys to GitHub!**

---

## Quick Start

1. Clone repo & install requirements
2. Configure `.env`, Google OAuth, and email
3. Run `python3 webapp.py`
4. Open in browser and enjoy!

---

For more details, see the code comments and documentation files.
