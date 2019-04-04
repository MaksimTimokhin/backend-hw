import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    USER = os.environ['POSTGRES_USER']
    PASSWORD = os.environ['POSTGRES_PASSWORD']
    HOST = os.environ['POSTGRES_HOST']
    DATABASE = os.environ['POSTGRES_DB']
    PORT = os.environ['POSTGRES_PORT']
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 