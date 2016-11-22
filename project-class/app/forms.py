from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class GetQuestion(Form):
    question = TextField('question')