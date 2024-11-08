import pyrebase
from api.config import config

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()