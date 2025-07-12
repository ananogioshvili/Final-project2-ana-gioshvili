from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from sqlalchemy.testing.pickleable import User
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            SubmitField, FileField,)
from wtforms.validators import DataRequired, length, ValidationError


class SignUpForm(FlaskForm):
    image = FileField()
    name = StringField("Name:", validators=[DataRequired()])
    surname = StringField("Surname:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    phone = IntegerField("+995 555 55 55 55")
    # date = DateField(validators=[DataRequired()])
    # country = SelectField(choices=["Choose country:", "Georgia", "Italy", "Spain", "France"], validators=[DataRequired()])
    # gender = RadioField("Choose gender:", choices=["Male", "Female"], validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired(), length(min=8, max=20)])

    submit = SubmitField("Sign up")



class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])

    submit = SubmitField("Login")


class MovieForm(FlaskForm):
    image = FileField("Add movie photo", validators=[FileAllowed(["jpg", "jpeg", "png", "gif"])])
    name = StringField("Add movie name", validators=[DataRequired()])
    year = IntegerField("Add movie release year", validators=[DataRequired()])

    submit = SubmitField("Add movie")
