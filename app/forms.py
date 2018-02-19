from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    subject=StringField('Subject',validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    button = SubmitField('Send')