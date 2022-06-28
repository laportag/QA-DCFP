from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class PlantForm(FlaskForm):
    com_name = StringField("Common Name")
    sci_name = StringField("Scientific Name")
    submit = SubmitField("Submit")

class GardenForm(FlaskForm):
    address = StringField("Address")
    submit = SubmitField("Submit")

class AddressForm(FlaskForm):
    # plant_id = IntegerField("Plant ID")
    address = IntegerField("Please enter Garden ID")
    submit = SubmitField("Submit")