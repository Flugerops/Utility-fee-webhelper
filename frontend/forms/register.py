from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    StringField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Email,
)


class RegisterForm(FlaskForm):
    nickname = StringField(validators=[DataRequired(),])
    password = PasswordField(validators=[DataRequired(),])
    password_confirm = PasswordField(validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")