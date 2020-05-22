from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    remember_me = BooleanField("Me lembre")
    submit = SubmitField("Submit")


class RegistrationForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField(
        "Repita a senha", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Registrar-se")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Por favor use um usuário diferente")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Por favor use um email diferente.")


class EditProfileForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    about_me = TextAreaField("Sobre mim", validators=[Length(min=0, max=140)])
    submit = SubmitField("Submit")
