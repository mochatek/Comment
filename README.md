# Comment App (Zoho Assessment)

## Stack

- Server: Flask ( _Python_ )
- Database: SQLite
- Frontend: HTML, CSS, Vanilla JS

## How to run ?

> **Prerequisites:** Python and Pip installed

1. Create virtual environment

```cmd
python -m venv env
```

2. Activate virtual environment

```cmd
env\Scripts\activate
```

3. Install dependancies

```cmd
pip install -r requirements.txt
```

4. Set up database and tables

```cmd
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

5. Start application server

```cmd
flask run
```

## Run as Docker Container !

> **Prerequisites:** Docker installed

1. Build image

```docker
docker built -t comment_img .
```

2. Start container

```docker
docker run -d -p 80:5000 --name comment comment_img
```
