from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from random import randint
from flask import render_template


class GetQuestion(Form):
    question = TextField('question')
    