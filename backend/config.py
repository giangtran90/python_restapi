import os
from dotenv import load_dotenv

# giup nhan key o file .env
load_dotenv()
SECRET_KEY = os.environ.get('KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
# Khong hien thong bao khi lam viec voi SQLALCHEMY
SQLALCHEMY_TRACK_MODIFICATIONS = False