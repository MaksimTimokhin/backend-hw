from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import pika

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
mail = Mail(app)
while True:
    try:
        connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@rabbitmq:5672'))
        break
    except:
        pass
channel = connection.channel()
channel.queue_declare(queue='emails')

from app import routes, models
