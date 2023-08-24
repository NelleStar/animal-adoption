from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange

class NewPetForm(FlaskForm):
    """form for adding pets"""

    name = StringField("Pet Name",
                       validators=[InputRequired(message='Name cannot be blank')])
    species = StringField('Species',
                          validators=[InputRequired(message='Species cannot be blank')])
    photo_url = StringField('Photo URL',
                            validators=[URL()])
    age = IntegerField('Pet Age In Years',
                       validators=[NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = BooleanField("Is this pet ready for adoption?")

class EditPetForm(FlaskForm):
    """Form for editingpets"""

    photo_url = StringField('Photo URL',
                            validators=[URL()])
    notes = StringField('Notes')
    available = BooleanField("Is this pet ready for adoption?")