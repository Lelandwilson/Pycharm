from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, IPAddress, number_range

from wtforms import validators, ValidationError

SensorLabels = [
    [],   #Zero
    ['','U1S1','U1S2','U1S3','U1S4','U1S5','U1S6','U1S7','U1S8','U1S9','U1S10','U1S11','U1S12','U1S13','U1S14',],   #Unit 1
    ['','U2S1','U2S2','U2S3','U2S4','U2S5','U2S6','U2S7','U2S8','U2S9','U2S10','U2S11','U2S12','U2S13','U2S14',],   #Unit 2
    ['','U3S1','U3S2','U3S3','U3S4','U3S5','U3S6','U3S7','U3S8','U3S9','U3S10','U3S11','U3S12','U3S13','U3S14',],   #Unit 3
    ['','U4S1','U4S2','U4S3','U4S4','U4S5','U4S6','U4S7','U4S8','U4S9','U4S10','U4S11','U4S12','U4S13','U4S14',],   #Unit 4
    ['','U5S1','U5S2','U5S3','U5S4','U5S5','U5S6','U5S7','U5S8','U5S9','U5S10','U5S11','U5S12','U5S13','U5S14',],   #Unit 5
    ['','U6S1','U6S2','U6S3','U6S4','U6S5','U6S6','U6S7','U6S8','U6S9','U6S10','U6S11','U6S12','U6S13','U6S14',],   #Unit 6
    ['','U7S1','U7S2','U7S3','U7S4','U7S5','U7S6','U7S7','U7S8','U7S9','U7S10','U7S11','U7S12','U7S13','U7S14',],   #Unit 7
    ['','U8S1','U8S2','U8S3','U8S4','U8S5','U8S6','U8S7','U8S8','U8S9','U8S10','U8S11','U8S12','U8S13','U8S14',],   #Unit 8
    ['','U9S1','U9S2','U9S3','U9S4','U9S5','U9S6','U9S7','U9S8','U9S9','U9S10','U9S11','U9S12','U9S13','U9S14',],   #Unit 9
    ['','U10S1','U10S2','U10S3','U10S4','U10S5','U10S6','U10S7','U10S8','U10S9','U10S10','U10S11','U10S12','U10S13','U10S14',]   #Unit 10
]

class SettingsForm1(FlaskForm):
    U1_S1 =  StringField('Unit 1 Sensor 1', validators=[DataRequired()])
    U1_S2 =  StringField('Unit 1 Sensor 2', validators=[DataRequired()])
    U1_S3 =  StringField('Unit 1 Sensor 3', validators=[DataRequired()])
    U1_S4 =  StringField('Unit 1 Sensor 4', validators=[DataRequired()])
    U1_S5 =  StringField('Unit 1 Sensor 5', validators=[DataRequired()])
    U1_S6 =  StringField('Unit 1 Sensor 6', validators=[DataRequired()])
    U1_S7 =  StringField('Unit 1 Sensor 7', validators=[DataRequired()])
    U1_S8 =  StringField('Unit 1 Sensor 8', validators=[DataRequired()])
    U1_S9 =  StringField('Unit 1 Sensor 9', validators=[DataRequired()])
    U1_S10 = StringField('Unit 1 Sensor 10', validators=[DataRequired()])
    U1_S11 = StringField('Unit 1 Sensor 11', validators=[DataRequired()])
    U1_S12 = StringField('Unit 1 Sensor 12', validators=[DataRequired()])
    U1_S13 = StringField('Unit 1 Sensor 13', validators=[DataRequired()])
    U1_S14 = StringField('Unit 1 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm2(FlaskForm):
    U2_S1 =  StringField('Unit 2 Sensor 1', validators=[DataRequired()])
    U2_S2 =  StringField('Unit 2 Sensor 2', validators=[DataRequired()])
    U2_S3 =  StringField('Unit 2 Sensor 3', validators=[DataRequired()])
    U2_S4 =  StringField('Unit 2 Sensor 4', validators=[DataRequired()])
    U2_S5 =  StringField('Unit 2 Sensor 5', validators=[DataRequired()])
    U2_S6 =  StringField('Unit 2 Sensor 6', validators=[DataRequired()])
    U2_S7 =  StringField('Unit 2 Sensor 7', validators=[DataRequired()])
    U2_S8 =  StringField('Unit 2 Sensor 8', validators=[DataRequired()])
    U2_S9 =  StringField('Unit 2 Sensor 9', validators=[DataRequired()])
    U2_S10 = StringField('Unit 2 Sensor 10', validators=[DataRequired()])
    U2_S11 = StringField('Unit 2 Sensor 11', validators=[DataRequired()])
    U2_S12 = StringField('Unit 2 Sensor 12', validators=[DataRequired()])
    U2_S13 = StringField('Unit 2 Sensor 13', validators=[DataRequired()])
    U2_S14 = StringField('Unit 2 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm3(FlaskForm):
    U3_S1 =  StringField('Unit 3 Sensor 1', validators=[DataRequired()])
    U3_S2 =  StringField('Unit 3 Sensor 2', validators=[DataRequired()])
    U3_S3 =  StringField('Unit 3 Sensor 3', validators=[DataRequired()])
    U3_S4 =  StringField('Unit 3 Sensor 4', validators=[DataRequired()])
    U3_S5 =  StringField('Unit 3 Sensor 5', validators=[DataRequired()])
    U3_S6 =  StringField('Unit 3 Sensor 6', validators=[DataRequired()])
    U3_S7 =  StringField('Unit 3 Sensor 7', validators=[DataRequired()])
    U3_S8 =  StringField('Unit 3 Sensor 8', validators=[DataRequired()])
    U3_S9 =  StringField('Unit 3 Sensor 9', validators=[DataRequired()])
    U3_S10 = StringField('Unit 3 Sensor 10', validators=[DataRequired()])
    U3_S11 = StringField('Unit 3 Sensor 11', validators=[DataRequired()])
    U3_S12 = StringField('Unit 3 Sensor 12', validators=[DataRequired()])
    U3_S13 = StringField('Unit 3 Sensor 13', validators=[DataRequired()])
    U3_S14 = StringField('Unit 3 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm4(FlaskForm):
    U4_S1 =  StringField('Unit 4 Sensor 1', validators=[DataRequired()])
    U4_S2 =  StringField('Unit 4 Sensor 2', validators=[DataRequired()])
    U4_S3 =  StringField('Unit 4 Sensor 3', validators=[DataRequired()])
    U4_S4 =  StringField('Unit 4 Sensor 4', validators=[DataRequired()])
    U4_S5 =  StringField('Unit 4 Sensor 5', validators=[DataRequired()])
    U4_S6 =  StringField('Unit 4 Sensor 6', validators=[DataRequired()])
    U4_S7 =  StringField('Unit 4 Sensor 7', validators=[DataRequired()])
    U4_S8 =  StringField('Unit 4 Sensor 8', validators=[DataRequired()])
    U4_S9 =  StringField('Unit 4 Sensor 9', validators=[DataRequired()])
    U4_S10 = StringField('Unit 4 Sensor 10', validators=[DataRequired()])
    U4_S11 = StringField('Unit 4 Sensor 11', validators=[DataRequired()])
    U4_S12 = StringField('Unit 4 Sensor 12', validators=[DataRequired()])
    U4_S13 = StringField('Unit 4 Sensor 13', validators=[DataRequired()])
    U4_S14 = StringField('Unit 4 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm5(FlaskForm):
    U5_S1 =  StringField('Unit 5 Sensor 1', validators=[DataRequired()])
    U5_S2 =  StringField('Unit 5 Sensor 2', validators=[DataRequired()])
    U5_S3 =  StringField('Unit 5 Sensor 3', validators=[DataRequired()])
    U5_S4 =  StringField('Unit 5 Sensor 4', validators=[DataRequired()])
    U5_S5 =  StringField('Unit 5 Sensor 5', validators=[DataRequired()])
    U5_S6 =  StringField('Unit 5 Sensor 6', validators=[DataRequired()])
    U5_S7 =  StringField('Unit 5 Sensor 7', validators=[DataRequired()])
    U5_S8 =  StringField('Unit 5 Sensor 8', validators=[DataRequired()])
    U5_S9 =  StringField('Unit 5 Sensor 9', validators=[DataRequired()])
    U5_S10 = StringField('Unit 5 Sensor 10', validators=[DataRequired()])
    U5_S11 = StringField('Unit 5 Sensor 11', validators=[DataRequired()])
    U5_S12 = StringField('Unit 5 Sensor 12', validators=[DataRequired()])
    U5_S13 = StringField('Unit 5 Sensor 13', validators=[DataRequired()])
    U5_S14 = StringField('Unit 5 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm6(FlaskForm):
    U6_S1 =  StringField('Unit 6 Sensor 1', validators=[DataRequired()])
    U6_S2 =  StringField('Unit 6 Sensor 2', validators=[DataRequired()])
    U6_S3 =  StringField('Unit 6 Sensor 3', validators=[DataRequired()])
    U6_S4 =  StringField('Unit 6 Sensor 4', validators=[DataRequired()])
    U6_S5 =  StringField('Unit 6 Sensor 5', validators=[DataRequired()])
    U6_S6 =  StringField('Unit 6 Sensor 6', validators=[DataRequired()])
    U6_S7 =  StringField('Unit 6 Sensor 7', validators=[DataRequired()])
    U6_S8 =  StringField('Unit 6 Sensor 8', validators=[DataRequired()])
    U6_S9 =  StringField('Unit 6 Sensor 9', validators=[DataRequired()])
    U6_S10 = StringField('Unit 6 Sensor 10', validators=[DataRequired()])
    U6_S11 = StringField('Unit 6 Sensor 11', validators=[DataRequired()])
    U6_S12 = StringField('Unit 6 Sensor 12', validators=[DataRequired()])
    U6_S13 = StringField('Unit 6 Sensor 13', validators=[DataRequired()])
    U6_S14 = StringField('Unit 6 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm7(FlaskForm):
    U7_S1 =  StringField('Unit 7 Sensor 1', validators=[DataRequired()])
    U7_S2 =  StringField('Unit 7 Sensor 2', validators=[DataRequired()])
    U7_S3 =  StringField('Unit 7 Sensor 3', validators=[DataRequired()])
    U7_S4 =  StringField('Unit 7 Sensor 4', validators=[DataRequired()])
    U7_S5 =  StringField('Unit 7 Sensor 5', validators=[DataRequired()])
    U7_S6 =  StringField('Unit 7 Sensor 6', validators=[DataRequired()])
    U7_S7 =  StringField('Unit 7 Sensor 7', validators=[DataRequired()])
    U7_S8 =  StringField('Unit 7 Sensor 8', validators=[DataRequired()])
    U7_S9 =  StringField('Unit 7 Sensor 9', validators=[DataRequired()])
    U7_S10 = StringField('Unit 7 Sensor 10', validators=[DataRequired()])
    U7_S11 = StringField('Unit 7 Sensor 11', validators=[DataRequired()])
    U7_S12 = StringField('Unit 7 Sensor 12', validators=[DataRequired()])
    U7_S13 = StringField('Unit 7 Sensor 13', validators=[DataRequired()])
    U7_S14 = StringField('Unit 7 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm8(FlaskForm):
    U8_S1 =  StringField('Unit 8 Sensor 1', validators=[DataRequired()])
    U8_S2 =  StringField('Unit 8 Sensor 2', validators=[DataRequired()])
    U8_S3 =  StringField('Unit 8 Sensor 3', validators=[DataRequired()])
    U8_S4 =  StringField('Unit 8 Sensor 4', validators=[DataRequired()])
    U8_S5 =  StringField('Unit 8 Sensor 5', validators=[DataRequired()])
    U8_S6 =  StringField('Unit 8 Sensor 6', validators=[DataRequired()])
    U8_S7 =  StringField('Unit 8 Sensor 7', validators=[DataRequired()])
    U8_S8 =  StringField('Unit 8 Sensor 8', validators=[DataRequired()])
    U8_S9 =  StringField('Unit 8 Sensor 9', validators=[DataRequired()])
    U8_S10 = StringField('Unit 8 Sensor 10', validators=[DataRequired()])
    U8_S11 = StringField('Unit 8 Sensor 11', validators=[DataRequired()])
    U8_S12 = StringField('Unit 8 Sensor 12', validators=[DataRequired()])
    U8_S13 = StringField('Unit 8 Sensor 13', validators=[DataRequired()])
    U8_S14 = StringField('Unit 8 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm9(FlaskForm):
    U9_S1 =  StringField('Unit 9 Sensor 1', validators=[DataRequired()])
    U9_S2 =  StringField('Unit 9 Sensor 2', validators=[DataRequired()])
    U9_S3 =  StringField('Unit 9 Sensor 3', validators=[DataRequired()])
    U9_S4 =  StringField('Unit 9 Sensor 4', validators=[DataRequired()])
    U9_S5 =  StringField('Unit 9 Sensor 5', validators=[DataRequired()])
    U9_S6 =  StringField('Unit 9 Sensor 6', validators=[DataRequired()])
    U9_S7 =  StringField('Unit 9 Sensor 7', validators=[DataRequired()])
    U9_S8 =  StringField('Unit 9 Sensor 8', validators=[DataRequired()])
    U9_S9 =  StringField('Unit 9 Sensor 9', validators=[DataRequired()])
    U9_S10 = StringField('Unit 9 Sensor 10', validators=[DataRequired()])
    U9_S11 = StringField('Unit 9 Sensor 11', validators=[DataRequired()])
    U9_S12 = StringField('Unit 9 Sensor 12', validators=[DataRequired()])
    U9_S13 = StringField('Unit 9 Sensor 13', validators=[DataRequired()])
    U9_S14 = StringField('Unit 9 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class SettingsForm10(FlaskForm):
    U10_S1 =  StringField('Unit 10 Sensor 1', validators=[DataRequired()])
    U10_S2 =  StringField('Unit 10 Sensor 2', validators=[DataRequired()])
    U10_S3 =  StringField('Unit 10 Sensor 3', validators=[DataRequired()])
    U10_S4 =  StringField('Unit 10 Sensor 4', validators=[DataRequired()])
    U10_S5 =  StringField('Unit 10 Sensor 5', validators=[DataRequired()])
    U10_S6 =  StringField('Unit 10 Sensor 6', validators=[DataRequired()])
    U10_S7 =  StringField('Unit 10 Sensor 7', validators=[DataRequired()])
    U10_S8 =  StringField('Unit 10 Sensor 8', validators=[DataRequired()])
    U10_S9 =  StringField('Unit 10 Sensor 9', validators=[DataRequired()])
    U10_S10 = StringField('Unit 10 Sensor 10', validators=[DataRequired()])
    U10_S11 = StringField('Unit 10 Sensor 11', validators=[DataRequired()])
    U10_S12 = StringField('Unit 10 Sensor 12', validators=[DataRequired()])
    U10_S13 = StringField('Unit 10 Sensor 13', validators=[DataRequired()])
    U10_S14 = StringField('Unit 10 Sensor 14', validators=[DataRequired()])
    submit = SubmitField("Save")

class NetworkForm(FlaskForm):
    interface =  StringField('Interface', validators=[DataRequired()])
    ip =  StringField('Ip Address', validators=[DataRequired(), IPAddress()])
    port =  StringField('Port', validators=[DataRequired(), number_range(0,10000)])
    router =  StringField('Router', validators=[DataRequired(), IPAddress()])
    DNS =  StringField('DNS', validators=[DataRequired(), IPAddress()])
    SSID =  StringField('SSID', validators=[])
    password = StringField('Password', validators=[])
    submit = SubmitField("Save")
