from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from wtforms.validators import InputRequired, Length # type: ignore

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)])
    submit = SubmitField('Register')
