from flask import redirect, render_template, url_for
from flask_login import login_required
from app import app
from app.models.db.db_model import User
from app.models.forms.user_form import UserForm
from app.services.session_scope import session_scope

@app.route('/users', methods=['GET'])
@login_required
def getUsers():
    with session_scope() as session:
        users = session.query(User).all()
    return render_template('user/users.html', users=users)

# Update
@app.route('/user/update/<int:id>', methods=['GET', 'POST'])
def updateUser(id):
    form = UserForm()
    
    with session_scope() as session:
        user = session.query(User).filter_by(id=id).first()
    
    if form.validate_on_submit():
        # Logique de mise à jour
        with session_scope() as session:
            user = session.query(User).filter_by(id=id).first()
            user.username = form.username.data
            user.email = form.email.data
        return redirect(url_for('updateUser',id=id))
        
    return render_template('user/update.html', form = form, user = user)

# Delete
@app.route('/user/delete/<int:id>', methods=['POST'])
def deleteUser(id):
    with session_scope() as session:
        user = session.query(User).filter_by(id=id).first()
        session.delete(user)
    return redirect(url_for('getUsers'))