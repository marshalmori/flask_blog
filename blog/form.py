from flask_wtf import Form
from wtforms import validators, StringField
from author.form import RegisterForm

# Como a classe SetupForm herda a classe RegisterForm, ela tem todas
# as características de RegisterForm
class SetupForm(RegisterForm):
    name = StringField('Blog name', [
    validators.Required(),
    validators.Length(max=80)
    ])
