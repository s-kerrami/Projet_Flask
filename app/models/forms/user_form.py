from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=3)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Mot de passe', validators=[DataRequired(), Length(min=8)])