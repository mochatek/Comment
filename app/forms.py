from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import ValidationError
from .models import User, db


def must_be_unique(form, field):
    user = db.session.query(User).filter(User.email == field.data).first()
    if user:
        raise ValidationError('Sorry! This email is already taken')


class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[
                       DataRequired(message='Email is mandatory'), must_be_unique])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is mandatory'),
        Length(min=8, message='Password must have minimum 8 characters'),
        Regexp('^(?=\S{10,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])',
               message="Must contain atleast 1 number, uppercase letter and special character")
    ])
    secret = StringField('Secret', validators=[
                         DataRequired(message='Secret is mandatory')])


class SigninForm(FlaskForm):
    email = EmailField('Email', validators=[
                       DataRequired(message='Email is mandatory')])
    password = PasswordField('Password', validators=[
                             DataRequired(message='Password is mandatory')])


class ForgotPasswordForm(FlaskForm):
    email = EmailField('Email', validators=[
                       DataRequired(message='Email is mandatory')])
    secret = StringField('Secret', validators=[
                         DataRequired(message='Secret is mandatory')])


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[
        DataRequired(message='Cannot post blank comment!')])
