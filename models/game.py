class Game():
    
    def __init__(self):
        self.win_lookup = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"
        }

    def get_winner(self, player1, player2):
        
        winner = None

        if self.win_lookup[player1.choice.lower()] == player2.choice.lower(): 
            winner = player1
        elif self.win_lookup[player2.choice.lower()] == player1.choice.lower():
            winner = player2
        return winner
        