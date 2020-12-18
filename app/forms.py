from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class GetPlayerDataForm(FlaskForm):
    name = SelectField(label="Player Name", coerce=int)
    submit = SubmitField('Submit')