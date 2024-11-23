# Flask Firebase Authentication API

A secure REST API implementing token-based authentication using Flask, Firebase Authentication, and JWT tokens.

## Features

- Token-based authentication with JWT
- Firebase Authentication and Realtime Database integration
- Rate limiting protection (200/day, 50/hour)
- Input validation using Pydantic schemas
- Secure password requirements
- User session tracking
- CORS support
- Security headers

## Tech Stack

- Flask
- Firebase Authentication
- Firebase Realtime Database
- PyJWT
- Pydantic
- Flask-Limiter
- Flask-CORS
- Pyrebase

## Setup Instructions

1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```
2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements
```
4. Create a `.env` file in the root directory and add your Firebase configuration
```bash
FLASK_ENV=development
DEBUG=True
SECRET_KEY=your-secret-key-here
# Firebase Config
API_KEY=your-api-key
AUTH_DOMAIN=your-auth-domain
PROJECT_ID=your-project-id
STORAGE_BUCKET=your-storage-bucket
MSG_ID=your-messaging-sender-id
APP_ID=your-app-id
MEASURE_ID=your-measurement-id
DB_URL=your-database-url
```
5. Run the application
```bash
flask -app app run # or python app.py
```
```bash
# To run in debug mode
flask --app app run --debug
```

## Avaliable Routes
- `POST /auth/login` - User Login
- `POST /auth/signup` - User Registration
- `GET /auth/me` - Get Current User Profile
- `POST /auth/logout` - User Logout

## Firebase Setup
1.  Create a Firebase project in the Firebase Console
1. Enable Email/Password authentication
1. Create a Realtime Database
1. Copy the configuration details to your `.env` file