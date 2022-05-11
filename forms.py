from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat','Cat'),("dog","Dog"),("porcupine","Porcupine")],)
    url = StringField("Url", validators=[Optional(),URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0,max=30),Optional()])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = StringField(
        "Comments",
        validators=[Optional()],
    )

    available = BooleanField("Available?")