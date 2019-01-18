"""A SubtractSquareState module, extends GameState"""
import copy
from gamestate import GameState


class SubtractSquareState(GameState):
    """
    a subclass of GameState (extends GameState) that can
    keep track of the state of a game of subtract square.
    """

    def __init__(self, p1_turn: bool) -> None:
        """
        Create a new SubtractSquareState, with first player p1
        if p1_turn is true.
        """
        self.p1_starts = p1_turn
        self._turn = 1
        self.current_value = int(input('Enter the number to subtract from: '))

    def __eq__(self, other: 'SubtractSquareState') -> bool:
        """
        Return whether SubtractSquareState self is equivalent
        to SubtractSquareState other.
        ** Docstring examples omitted due to requiring input().
        """
        return type(self) == type(other) and self._turn == other._turn \
            and self.current_value == other.current_value

    def __str__(self)-> str:
        """
        Return a str representation of SubtractSquareState self.
        Overrides GameState's string method.
        The state is represented as a string of the
        current game value.
        ** Docstring examples omitted due to requiring input().
        """
        return "The current value is {}".format(str(self.current_value))

    def get_possible_moves(self) -> list:
        """
        Return a list of possible moves in SubtractSquareState self
        ** Docstring examples omitted due to requiring input()
        """
        current_value = self.current_value
        i = 1
        possible_moves = []
        while i**2 <= current_value:
            possible_moves.append(i**2)
            i += 1
        return possible_moves

    def is_valid_move(self, move: int) -> bool:
        """
        Return whether move is a valid move in the GameState self
        ** Docstring examples omitted due to requiring input().
        """
        possible_moves = self.get_possible_moves()
        if move in possible_moves:
            return True
        return False

    def get_current_player_name(self) -> str:
        """
        Return the current player, p1 or p2
        ** Docstring examples omitted due to requiring input()
        """
        return GameState.get_current_player_name(self)

    def make_move(self, move_to_make: int)->'SubtractSquareState':
        """
        Makes the move move_to_make on SubtractSquareState self.
        ** Docstring examples omitted due to requiring input().
        """
        new = copy.copy(self)
        new._turn += 1
        new.current_value -= move_to_make
        return new


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
