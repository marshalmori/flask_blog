from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField
from author.form import RegisterForm
from blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField

# Como a classe SetupForm herda a classe RegisterForm, ela tem todas
# as características de RegisterForm
class SetupForm(RegisterForm):
    name = StringField('Blog name', [
    validators.Required(),
    validators.Length(max=80)
    ])

def categories():
    return Category.query

class PostForm(FlaskForm):
    title = StringField('Title', [
        validators.Required(),
        validators.Length(max=80)
        ])
    body = TextAreaField('Content', validators=[validators.Required()])
    category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
    new_category = StringField('New Category')
