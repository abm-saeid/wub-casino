from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, SelectField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    link = StringField("Facebook ID Link", validators=[DataRequired()])
    promo = StringField("Promo Code")
    submit = SubmitField("Submit")

class CoinFlip(FlaskForm):
    id_num = StringField("ID", validators=[DataRequired()])
    prediction = RadioField("Prediction", choices=[('1','Heads'),('2','Tails')], validators=[DataRequired()])
    bet_amount = IntegerField("Bet Amount", validators=[DataRequired()])
    submit = SubmitField("Bet")

class Dice(FlaskForm):
    id_num = StringField("ID", validators=[DataRequired()])
    bet_amount = IntegerField("Bet Amount", validators=[DataRequired()])
    submit = SubmitField("Bet")

class Roulette(FlaskForm):
    id_num = StringField("ID", validators=[DataRequired()])
    prediction = IntegerField("Prediction for number",validators=[DataRequired()])
    color = RadioField("Prediction for color", choices=[('1', 'Black'),('2', 'White')], validators=[DataRequired()])
    bet_amount = IntegerField("Bet Amount", validators=[DataRequired()])
    submit = SubmitField("Bet")

class Slots(FlaskForm):
    id_num = StringField("ID", validators=[DataRequired()])
    bet_amount = IntegerField("Bet Amount", validators=[DataRequired()])
    submit = SubmitField("Bet")
    

class Ludo(FlaskForm):
    id1 = StringField("First", validators=[DataRequired()])
    id2 = StringField("Second", validators=[DataRequired()])
    id3 = StringField("Third", validators=[DataRequired()])
    id4 = StringField("Fourth", validators=[DataRequired()])
    bet_amount = IntegerField("Bet Amount", validators=[DataRequired()])
    submit = SubmitField("Bet")

class Search(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    submit = SubmitField("Search")