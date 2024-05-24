
from flask import redirect, render_template, url_for
from flask_login import login_user, logout_user
from app import app, login_manager
from app.models.db.db_model import User
from app.models.forms.login_form import LoginForm
from app.models.forms.user_form import UserForm
from app.services.session_scope import session_scope
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(id):
    with session_scope() as session:
        return session.query(User).filter_by(id=id).first()

@app.route('/auth/register', methods=['GET','POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        
        try:
            with session_scope() as session:
                session.add(new_user)
        except Exception as error:
            print(f"Une erreur s'est produite lors de l'ajout de l'utilisateur : \n {error}")
            return redirect(url_for('index'))
        
        return redirect(url_for('login'))
    return render_template('auth/register.html', form=form)

@app.route('/auth/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        try:
            with session_scope() as session:
                user = session.query(User).filter_by(email=form.email.data).first()
                if user and check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    print(("erreur useur | password"))
                    return render_template('auth/login.html', form=form)
        except Exception as error:
            print(f"Une erreur s'est produite lors du login de l'utilisateur : \n {error}")
            return redirect(url_for('login'))
    return render_template('auth/login.html', form=form)

@app.route('/auth/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))