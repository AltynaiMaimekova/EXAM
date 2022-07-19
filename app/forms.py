from flask_wtf import FlaskForm
from wtforms import validators
import wtforms as wf


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField(label='Пароль', validators=[
        validators.DataRequired(),
        validators.Length(min=8)
    ])
    submit = wf.SubmitField('Ok')


class EmployeeForm(FlaskForm):
    fullname = wf.StringField('Имя', validators=[wf.validators.DataRequired()])
    phone = wf.StringField('Телефон', validators=[wf.validators.DataRequired()])
    short_info = wf.TextAreaField('Краткое био', validators=[wf.validators.DataRequired()])
    experience = wf.IntegerField('Опыт работы', validators=[wf.validators.DataRequired()])
    preferred_position = wf.StringField('Позиция')
    submit = wf.SubmitField('Ok')

    def validate(self):
        if not super().validate():
            return False
        if ' ' not in self.fullname.data:
            self.fullname.errors.append('Имя должно содержать пробел')
            return False
        return True


