from app import app
from flask import render_template,request

from forms import GetQuestion

from random import randint

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/8ball', methods=['GET', 'POST'])
def get_question():
    form = GetQuestion()
    if request.method == 'POST':
        choice = randint(1,3)
        if choice ==1:
            response = "It is certain"
        if choice ==2:
            response = "It is decidedly so"
        if choice ==3:
            response = "Without a doubt"
        return render_template('index.html', form=form,response=response )
    if request.method == 'GET':	
		return render_template('index.html', form=form)
   
