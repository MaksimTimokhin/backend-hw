import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pika
from itsdangerous import URLSafeTimedSerializer

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer('innprak-2019')
    return serializer.dumps(email, salt='tututuinnpraksalt')

addr = "backend.hw"
password = r"innprak-2019"
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(addr, password)

while True:
    try:
        connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@rabbitmq:5672'))
        break
    except:
        pass
channel = connection.channel()

channel.queue_declare(queue='emails')

def callback(ch, method, properties, body):
    email = body.decode()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Please confirm your email"
    msg['From'] = addr
    msg['To'] = email
    token = generate_confirmation_token(email)
    url = 'http://127.0.0.1:5000/confirm/' + token
    html = f'''
    <p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p>
    <p><a href="{url}">{url}</a></p>
    <br>
    <p>Cheers!</p>
    '''
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    s.sendmail(addr, email, msg.as_string())

    
channel.basic_consume(queue='emails',
                      on_message_callback=callback)

channel.start_consuming()
