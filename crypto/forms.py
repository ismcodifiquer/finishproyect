from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField, RadioField, Field
from wtforms.validators import DataRequired, Length, InputRequired
from wtforms.widgets import TextArea

cryptos =[('EUR', 'EUR'), ('BTC','BTC'), ('ETH','ETH'), ('XRP','XRP'), ('LTC','LTC'), ('BCH','BCH'), ('BNB','BNB'), ('USDT','USDT'), ('EOS','EOS'), ('BSV','BSV'), ('XLM','XLM'), ('ADA','ADA'), ('TRX','TRX')]

class CryptoForm(FlaskForm):
    From = SelectField('From', choices=cryptos)
    Q = StringField('Q', validators= [DataRequired()])
    To = SelectField('To', id='To', choices=cryptos)
    ToQ = Field('ToQ')






