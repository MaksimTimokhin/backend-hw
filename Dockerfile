FROM python:3.6-alpine

RUN adduser -D app

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 venv/bin/pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY app.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app.py

RUN chown -R app:app ./
USER app

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
