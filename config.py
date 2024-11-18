import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
DEBUG = os.environ.get('DEBUG', True)
SECRET_KEY = os.environ.get('SECRET_KEY', 'veryverysuperultrasecret')

FIREBASE_CONFIG = {
    'apiKey': os.environ.get('API_KEY'),
    'authDomain': os.environ.get('AUTH_DOMAIN'),
    'projectId': os.environ.get('PROJECT_ID'),
    'storageBucket': os.environ.get('STORAGE_BUCKET'),
    'messagingSenderId': os.environ.get('MSG_ID'),
    'appId': os.environ.get('APP_ID'),
    'measurementId': os.environ.get('MEASURE_ID'),
    'databaseURL': os.environ.get('DB_URL')
}

SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = False
PERMANENT_SESSION_LIFETIME = 1800 
