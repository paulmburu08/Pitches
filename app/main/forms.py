from flask_wtf import FlaskForm
from wtforms import TextAreaField

class AddComment(FlaskForm):

    comment = TextAreaField('Comment')