"""A strategy module"""
from typing import Any
from random import randint
from game import Game

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

# TODO: Implement a random strategy.


def random(game: Game) -> Any:
    """
    Return a random move for game.
    ** Docstring examples omitted due to requiring random().
    """
    possible_moves = game.current_state.get_possible_moves()
    return possible_moves[randint(0, len(possible_moves)-1)]


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
