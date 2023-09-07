from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, SubmitField, validators
from wtforms.validators import DataRequired

class InvoiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    client_name = StringField('Client Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    due_date = DateField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])
    number = StringField('Invoice#', validators=[DataRequired()])
    submit = SubmitField('Submit')