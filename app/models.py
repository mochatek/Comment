from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return db.session.query(User).filter(User.id == int(id)).first()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(20), nullable=True)
    secret = db.Column(db.String(20), nullable=False)

    def set_password(self):
        self.password_hash = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
