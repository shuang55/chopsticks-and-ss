"""a Game module"""
from typing import Any
from gamestate import GameState


class Game:
    """
    Create Game self, which can give instructions, tell if the Game
    is over, determine a winner, and convert a string to a move.
    p1_turn - True if p1 is the first player to make a move
    """
    p1_turn: bool

    def __init__(self, p1_turn: bool)->None:
        """Create a Game. Not meant to be instantiated on its own."""
        self.is_p1_turn = p1_turn
        self.current_state = None

    def __eq__(self, other: Any)-> bool:
        """Return if Game self is equal to Game other
         ** Docstring examples omitted as type Game is not meant to be
         instantiated
         """
        return type(self) == type(other) and \
            self.current_state == other.current_state

    def __str__(self) -> str:
        """return a string representation of Game self, which
        returns the current GameState
        ** Docstring examples omitted as type Game is not meant to
        be instantiated on its own.
        """
        return self.current_state.__str__()

    def is_over(self, state: GameState) -> bool:
        """Return whether Game self is over
        """
        raise NotImplementedError('subclass must be implemented!')

    def get_instructions(self) -> str:
        """
        return the instructions for Game self
        """
        raise NotImplementedError('subclass must be implemented!')

    def is_winner(self, player: str)-> bool:
        """
        Return whether player is a winner in Game Self
        """
        raise NotImplementedError('subclass must be implemented!')

    def str_to_move(self, move: 'str')->None:
        """
        Return the move to be made based on the str move.
        """
        raise NotImplementedError('Subclass must be implemented!')


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
