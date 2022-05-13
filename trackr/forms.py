from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange

class SaveItemForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    description = TextAreaField("Description", validators = [DataRequired()])
    price = FloatField("Price", validators = [InputRequired(), NumberRange(min = 0)])
    count = IntegerField("Count", validators = [InputRequired(), NumberRange(min = 0)])
    submit = SubmitField("Save")

class DeleteItemForm(FlaskForm):
    deletion_comment = TextAreaField("Deletion Comment")
    submit = SubmitField("Delete")
    