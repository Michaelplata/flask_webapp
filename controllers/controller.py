from app import app
from models.game import *
from models.player import *
from flask import render_template

# take url path placeholders
# store them as dictionary
# but for the controller take the placeholders and 
# use them as arguments for a function that takes 

@app.route('/<player1_choice>/<player2_choice>')
def get_winner(player1_choice, player2_choice):
    player1 = Player("player1", player1_choice) 
    player2 = Player("player2", player2_choice) 
    game = Game()
    winner = game.get_winner(player1, player2)
    return render_template("game.html", player1=player1, player2=player2, winner=winner)


@app.route('/welcome-page')
def index():
    return render_template('base.html')