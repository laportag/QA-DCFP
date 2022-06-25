from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class PlantForm(FlaskForm):
    com_name = StringField("Common Name")
    sci_name = StringField("Scientific Name")
    submit = SubmitField("Submit")

class GardenForm(FlaskForm):
    address = StringField("Address")
    submit = SubmitField("Submit")