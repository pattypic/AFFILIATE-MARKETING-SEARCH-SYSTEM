from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

# defines a form for adding or editing a link. The class has three fields defined
# name: A StringField that represents the name of the link. The label for the field is 'Name', and it is a required field
# url: A StringField that represents the URL of the link. The label for the field is 'URL', and it is also a required field.
# submit: A SubmitField that represents a submit button for the form. The label for the button is 'Save'.
class LinkForm(FlaskForm):
    searched = StringField('Search', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Save')