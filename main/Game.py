# Game code
from main.Player import Player


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.winner = ""

    def won_point(self, winner: Player):
        self.winner = winner

    def get_score(self) -> str:
        if self.winner == self.player1:
            return "Fifteen-Love"
        if self.winner == self.player2:
            return "Fifteen-All"
        return "Love-All"
