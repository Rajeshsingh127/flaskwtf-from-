from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,HiddenField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms.fields.html5 import EmailField
class Registerationform(FlaskForm):
    id = HiddenField()
    name = StringField('Name', validators=[DataRequired(),Length(min=5,max=20)])
    username = StringField('Username', validators=[DataRequired(),Length(min=5,max=20)])
    email = StringField('Email', validators=[DataRequired(),Length(min=5,max=20), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=5,max=20)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),Length(min=5,max=20),EqualTo('password')])
    submit = SubmitField('Signup')


class Loginform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=5,max=20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=5,max=20)])
    remember = BooleanField('Remember me ')
    submit = SubmitField('Login')
