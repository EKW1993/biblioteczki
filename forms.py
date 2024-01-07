from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField 
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()] )