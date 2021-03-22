import pytest
from main.Game import Game
from main.Player import Player


def create_game(player1: Player, player2: Player):
    return Game(player1, player2)


def create_player(name: str):
    return Player(name)


@pytest.mark.parametrize("score_player_1, score_player_2, expected_result", [
    (0, 0, "Love-All"),
    (1, 0, "Fifteen-Love"),
    (1, 1, "Fifteen-All"),
    (2, 1, "Thirty-Fifteen"),
    (2, 0, "Thirty-Love")
])
def test_game_score(score_player_1: int, score_player_2: int, expected_result: str) -> None:
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)

    score_max = max(score_player_1, score_player_2)
    for score in range(0, score_max):
        if score < score_player_1:
            game.won_point(player1)
        if score < score_player_2:
            game.won_point(player2)

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == expected_result
