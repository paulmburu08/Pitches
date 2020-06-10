from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,SelectField
from wtforms.validators import Required

class PitchesForm(FlaskForm):

    title =  StringField('Pitch Title', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    category = SelectField(u'Select Category', choices=[('pickup','Pickup lines'),('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')],validators=[Required()])
    submit = SubmitField('Submit')

class AddComment(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')