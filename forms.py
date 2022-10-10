from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired,Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username =  StringField('username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('password', 
                            validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('confirm_password', 
                            validators=[DataRequired(), Length(min=4), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('password', 
                            validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Remember_me')
    submit = SubmitField('Sign up')
