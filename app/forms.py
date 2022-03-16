from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[DataRequired()])
    property_description = TextAreaField('Property Description', validators=[DataRequired()])
    noOfRooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    noOfBathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    property_price = StringField('Property Price', validators=[DataRequired()])
    property_location = StringField('Property Location', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Flat', 'Flat')])
    property_image = FileField('Property Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])