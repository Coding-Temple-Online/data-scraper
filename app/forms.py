from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class GetPlayerDataForm(FlaskForm):
    names = SelectField(label="Player Name", coerce=int)
    submit = SubmitField('Submit')