"""a GameState module"""
from typing import Any


class GameState:
    """
    a superclass GameState that can play two-player,
    sequential move, zero-sum, perfect information games.
    p1_starts - True if p1 is the first player
    """
    p1_starts: bool

    def __init__(self, p1_starts: bool)-> None:
        """
        Initialize a GameState, (usually) not to be instantiated on its own...
        The subclass is where most of the gamestate is tracked.
        """
        self.p1_starts = p1_starts
        self._turn = 1

    def __eq__(self, other) -> bool:
        """Return whether GameState self is equal to other
        >>> m = GameState(True)
        >>> n = GameState(False)
        >>> m == n
        False
        """
        return type(self) == type(other) and \
            self._turn == other._turn and \
            self.p1_starts == other.p1_starts

    def __str__(self) -> str:
        """
        Return a string representation of GameState
        >>> m = GameState(True)
        >>> print(m)
        turn: 1
        """
        return "turn: {}".format(self._turn)

    def get_possible_moves(self) -> list:
        """Return a list of possible moves in GameState self"""
        raise NotImplementedError('subclass must be implemented!')

    # check the type of this one
    def is_valid_move(self, move: Any) -> None:
        """Return whether move is a valid move in the GameState self"""
        raise NotImplementedError('subclass must be implemented!')

    def get_current_player_name(self) -> str:
        """Return the current player, p1 or p2"""
        if self.p1_starts:
            if self._turn % 2 != 0:
                return 'p1'
            return 'p2'
        else:
            if self._turn % 2 != 0:
                return 'p2'
            return 'p1'

    def make_move(self, move_to_make: Any) -> None:
        """Return a new GameState with move_to_make applied to the
        GameState self
        """
        raise NotImplementedError('subclass must be implemented!')


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
