# Game code
from main.Player import Player


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.winner = ""

    def won_point(self, winner: Player):
        self.winner.add_point()
        self.winner = winner.name

    def get_score(self) -> str:
        if (self.player1.score - self.player2.score) == 0:
            if self.player1.score == 0:
                return "Love-All"
            elif self.player1.score == 1:
                return "Fifteen-All"
            elif self.player1.score == 2:
                return "Thirty-All"
            else:
                return "Deuce"
        if self.player1.score == 1:
            if self.player2.score == 0:
                return "Fifteen-Love"
            if self.player2.score == 2:
                return "Fifteen-Thirty"
            if self.player2.score == 3:
                return "Fifteen-Forty"
            else:
                return "Win for player 2"
