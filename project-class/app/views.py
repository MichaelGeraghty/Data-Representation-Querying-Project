from app import app
from flask import render_template,request

from forms import GetQuestion

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/8ball', methods=['GET', 'POST'])
def get_question():
    form = GetQuestion()
    return render_template('index.html', form=form)
