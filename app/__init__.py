from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

db_migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'signin'


csrf = CSRFProtect(app)

csp = {
    'default-src': '\'self\'',
    'script-src': ['\'self\''],
    'font-src': ['\'self\'', 'cdnjs.cloudflare.com'],
    'style-src': ['\'self\'', 'cdnjs.cloudflare.com'],
    'img-src': ['\'self\'', 'placehold.jp']
}

# If server is running on HTTPS, set values to True
talisman = Talisman(app, content_security_policy=csp,
                    force_https=False, session_cookie_secure=False)

from . import routes  # nopep8
