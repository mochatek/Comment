from . import app, db
from .models import User, Comment
from .forms import SigninForm, SignupForm, ForgotPasswordForm, CommentForm
from flask_login import login_user, logout_user, current_user, login_required
from flask import request, render_template, redirect, url_for, flash, jsonify
from werkzeug.exceptions import HTTPException


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = SignupForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password=form.password.data, secret=form.secret.data)
        user.set_password()
        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering. Please Sign In to continue',
              category='success')
        return redirect(url_for('signin'))

    return render_template('signup.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = SigninForm()

    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.email == form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('email-password mismatch !', category='error')

    return render_template('signin.html', form=form)


@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = ForgotPasswordForm()
    password = None

    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.email == form.email.data, User.secret == form.secret.data).first()

        if user:
            password = user.password
        else:
            flash('email-secret mismatch !', category='error')

    return render_template('forgotpassword.html', form=form, password=password)


@app.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('signin'))


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(text=form.text.data, by=current_user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('index', comment_filter='mine', newPost=True))

    newPost = request.args.get('newPost', False)
    comment_filter = request.args.get('comment_filter', 'others')
    comments = []

    if comment_filter == 'others':
        comments = db.session.query(Comment).filter(
            Comment.by != current_user.id).order_by(Comment.on.desc()).all()
    else:
        comments = db.session.query(Comment).filter(
            Comment.by == current_user.id).order_by(Comment.on.desc()).all()

    return render_template('index.html', form=form, comments=comments, comment_filter=comment_filter, newPost=newPost)


@app.errorhandler(HTTPException)
def error(e):
    return render_template('error.html', code=e.code, name=e.name, description=e.description), e.code
