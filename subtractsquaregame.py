"""a subtractsquareGame module - a subclass of Game"""
from typing import Any
from game import Game
from subtractsquarestate import SubtractSquareState


class SubtractSquareGame(Game):
    """
    A class to play subtractsquare - is a subclass of (extends) class Game
    """

    def __init__(self, p1_turn: bool) -> None:
        """Create a new SubtractSquareGame, with
        p1 being the first player if p1_turn is true.
        ** docstring examples omitted due to requiring input().
        """
        self.current_state = SubtractSquareState(p1_turn)

    def __eq__(self, other: Any)-> bool:
        """Return whether SubtractSquareGame self is equal to other
        ** docstring examples omitted due to requiring input().
        """
        return Game.__eq__(self, other)

    def __str__(self)-> str:
        """Return a string representaiton of SubtractSquareGame self, which
        prints the current state of the game
        ** docstring examples omitted due to requiring input().
        """
        return self.current_state.__str__()

    def is_over(self, state: SubtractSquareState)-> bool:
        """Return whether SubtractSquareGame self is over.
        ** docstring examples omitted due to requiring input().
        """
        return state.current_value == 0

    def is_winner(self, player: str)-> bool:
        """
        Return whether player is the winner.
        ** docstring examples omitted due to requiring input().
        """
        if self.current_state.current_value != 0:
            return False
        return self.current_state.get_current_player_name() != player

    def str_to_move(self, move: str)-> int:
        """
        precondition: move must be the string representation of some integer
        Return the integer representation of move.
        ** Docstring examples omitted due to requiring input().
        """
        return int(move)

    def get_instructions(self) -> str:
        """Return the instructions for SubtractSquareGame self.
        ** Docstring examples omitted due to requiring input().
        """
        return ('A non-negative whole number is chosen as the ' +
                'starting value, by a player.' +
                ' The player whose turn it is choose some square of a ' +
                'positive whole number to subtract.' +
                ' The chosen square must not be larger than the value. After ' +
                'subtracting, we have a new value' +
                ' and the next player chooses a square to subtract from it.' +
                ' Play continues (alternating between players) ' +
                'until no moves are possible.' +
                ' Whoever is about to play at that point is the loser!')


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
