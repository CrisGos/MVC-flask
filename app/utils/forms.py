from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField,TextAreaField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    mac_address = StringField('Mac Address', validators=[DataRequired()])
    serial_number = IntegerField('Serial Number', validators=[DataRequired()])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    description = TextAreaField('Description')