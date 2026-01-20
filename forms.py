from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class NGOForm(FlaskForm):
    name = StringField("NGO Name", validators=[DataRequired()])
    trustees = TextAreaField("Trustees", validators=[DataRequired()])
    submit = SubmitField("Submit")
