from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from ..models import User

class CommentForm(FlaskForm):

    # title = StringField('Review title',validators=[Required()])
    comment = TextAreaField('Blog comment', validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddBlogForm(FlaskForm):
    content = TextAreaField ('Blog', validators = [Required()])
    submit = SubmitField('SUBMIT')

class SubscriptionForm(FlaskForm):
   name=StringField('Name',validators =[Required()])
   email=StringField('Email',validators =[Required()])
   submit = SubmitField('Submit')

# class UpdatePostForm(FlaskForm):
#    title=StringField('Title',validators = [Required()])
#    content=TextAreaField('Content',validators = [Required()])
#    submit=SubmitField('SUBMIT')