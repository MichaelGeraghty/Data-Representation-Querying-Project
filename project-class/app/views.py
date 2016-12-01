from app import app
from flask import render_template,request,jsonify

from random import randint

"""@app.route('/lotto/')
def new_numbers():
    game_nums = []
    while len(game_nums) < 6:
        n = randint(1,47)
        if not n in game_nums:
            game_nums.append(n)
            game_nums.sort()
    return jsonify(result1=game_nums)
 """   
 
@app.route('/8ball/')
def get_answer():
        quest = request.args.get('question')
        choice = randint(1,20)
        #https://en.wikipedia.org/wiki/Magic_8-Ball
        if choice ==1:
            response = "It is certain"
        elif choice ==2:
            response = "It is decidedly so"
        elif choice ==3:
            response = "Without a doubt"
        elif choice ==4:
            response = "Yes, definitely"
        elif choice ==5:
            response = "You may rely on it"
        elif choice ==6:
            response = "As I see it, yes"
        elif choice ==7:
            response = "Most likely"
        elif choice ==8:
            response = "Outlook good"
        elif choice ==9:
            response = "Yes"
        elif choice ==10:
            response = "Signs point to yes"
        elif choice ==11:
            response = "Reply hazy try again"
        elif choice ==12:
            response = "Ask again later"
        elif choice ==13:
            response = "Better not tell you now"
        elif choice ==14:
            response = "Cannot predict now"
        elif choice ==15:
            response = "Concentrate and ask again"
        elif choice ==16:
            response = "Don't count on it"
        elif choice ==17:
            response = "My reply is no"
        elif choice ==18:
            response = "My sources say no"
        elif choice ==19:
            response = "Outlook not so good"
        elif choice ==20:
            response = "Very doubtful"
        return jsonify(result=response)
     
@app.route('/')
def index():
    game_nums = []
    while len(game_nums) < 6:
        n = randint(1,47)
        if not n in game_nums:
            game_nums.append(n)
            game_nums.sort()
    return render_template('index.html',game_nums = game_nums)

@app.route('/die/')
def get_die():
    a = randint(1,6)
    b = randint(1,6)
    return jsonify(result2 = a, result3 = b) 
