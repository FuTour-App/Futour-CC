import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'apiKey': os.environ.get('API_KEY'),
    'authDomain': os.environ.get('AUTH_DOMAIN'),
    'projectId': os.environ.get('PROJECT_ID'),
    'storageBucket': os.environ.get('STORAGE_BUCKET'),
    'messagingSenderId': os.environ.get('MSG_ID'),
    'appId': os.environ.get('APP_ID'),
    'measurementId': os.environ.get('MEASURE_ID'),
    'signInFlow': os.environ.get('FLOW'),
    'databaseURL': os.environ.get('DB_URL')
}
