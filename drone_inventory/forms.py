#where user login form lives

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm): #   inherits from FlaskForm
    #email, password, first_name, last_name
    email = StringField('Email', validators=[DataRequired(), Email()]) #'Email' is label #Email() uses regex to confirm email format
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    password = PasswordField('Password', validators = [DataRequired()]) #DataRequired() with no following parameter just means ANYTHING needs to be in there to validate
    submit_button = SubmitField()

class DroneForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price', places=2) #places is # of decimals
    camera_quality = StringField('camera quality')
    flight_time = StringField('flight time')
    max_speed = StringField('max speed')
    dimensions = StringField('dimensions')
    weight = StringField('weight')
    cost_of_production = DecimalField('cost of production', places=2)
    series = StringField('series')
    submit_button = SubmitField()
