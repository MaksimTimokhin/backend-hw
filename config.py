import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'innprak-2019'
    
    USER = os.environ['POSTGRES_USER']
    PASSWORD = os.environ['POSTGRES_PASSWORD']
    HOST = os.environ['POSTGRES_HOST']
    DATABASE = os.environ['POSTGRES_DB']
    PORT = os.environ['POSTGRES_PORT']
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    
    SECURITY_PASSWORD_SALT = 'tututuinnpraksalt'
    
    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = 'backend.hw'
    MAIL_PASSWORD = 'innprak-2019'

    # mail accounts
    MAIL_DEFAULT_SENDER = 'backend.hw@gmail.com'

    
