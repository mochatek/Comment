FROM python:3.9

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN pip install gunicorn==20.0.4

COPY . /app/

ENV FLASK_APP=wsgi.py FLASK_ENV=production

EXPOSE 5000

RUN flask db init && flask db migrate && flask db upgrade

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
