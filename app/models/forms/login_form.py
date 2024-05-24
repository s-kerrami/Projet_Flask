import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError

def strong_password(form, field):
    password = field.data
    if len(password) < 8:
        raise ValidationError("Le mot de passe doit contenir au minimum 8 caractères.")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Doit contenir au moins une majuscule.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Doit contenir au moins une minuscule.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Doit contenir au moins un nombre.")
    if not re.search(r"[!@#$^&*(),.?\":{}|<>%]", password):
        raise ValidationError("Doit contenir au moins un caractère spécial.")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Champ email obligatoire !!!"), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired("Champ password obligatoire !!!"), strong_password])