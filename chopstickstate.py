"""A ChopstickState module, extends superclass GameState"""
import copy
from gamestate import GameState


class ChopstickState(GameState):
    """
    a subclass of GameState (extends GameState)
     that can keep track of a game of Chopsticks
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Create a ChopstickState self with first player p1 if p1_starts.
        >>> m = ChopstickState(True)
        >>> print(m)
        Player 1: 1-1; Player 2: 1-1
        """
        self.p1_starts = p1_starts
        self._turn = 1
        self.p1l = 1
        self.p2l = 1
        self.p1r = 1
        self.p2r = 1

    def __eq__(self, other: 'ChopstickState') -> bool:
        """Returns whether ChopstickState self is
        equal to ChopstickState other
        >>> m = ChopstickState(True)
        >>> n = ChopstickState(True)
        >>> m == n
        True
        >>> n = n.make_move('ll')
        >>> m == n
        False
        """
        return (type(self) == type(other) and self._turn == other._turn
                and self.p1l == other.p1l and self.p2l == other.p2l and
                self.p2r == other.p2r and self.p1r == other.p1r)

    def __str__(self) -> str:
        """Return a str representation of ChopstickState self.
        Overrides GameState's string method.
        The string returned is a representation
        of the current game values (the values of each player's hands)
        >>> m = ChopstickState(True)
        >>> print(m)
        Player 1: 1-1; Player 2: 1-1
        """
        return "Player 1: {}-{}; Player 2: {}-{}".format(
            self.p1l, self.p1r, self.p2l, self.p2r)

    def get_possible_moves(self) -> list:
        """Return a list of possible moves in ChopstickState self
        >>> m = ChopstickState(True)
        >>> m = m.make_move('ll')
        >>> m = m.make_move('ll')
        >>> m = m.make_move('ll')
        >>> m.get_possible_moves()
        ['rr', 'rl']
        """
        moves = []
        if self.is_valid_move('ll'):
            moves.append('ll')
        if self.is_valid_move('lr'):
            moves.append('lr')
        if self.is_valid_move('rr'):
            moves.append('rr')
        if self.is_valid_move('rl'):
            moves.append('rl')
        return moves

    def is_valid_move(self, move: str) -> bool:
        """Return whether move is a valid move in the ChopstickState self
        >>> m = ChopstickState(True)
        >>> m = m.make_move('ll')
        >>> m = m.make_move('ll')
        >>> m.is_valid_move('ll')
        True
        >>> m = m.make_move('ll')
        >>> m.is_valid_move('ll')
        False
        """
        current_player = self.get_current_player_name()
        if move == 'll':
            if self.p1l != 0 and self.p2l != 0:
                return True
            return False
        elif move == 'rr':
            if self.p1r != 0 and self.p2r != 0:
                return True
            return False
        elif move == 'lr':
            if current_player == 'p1':
                if self.p1l != 0 and self.p2r != 0:
                    return True
                return False
            else:
                if self.p2l != 0 and self.p1r != 0:
                    return True
                return False
        elif move == 'rl':
            if current_player == 'p1':
                if self.p1r != 0 and self.p2l != 0:
                    return True
                return False
            else:
                if self.p2r != 0 and self.p1l != 0:
                    return True
                return False
        return False

    def get_current_player_name(self) -> str:
        """Return the current player, p1 or p2
        >>> m = ChopstickState(True)
        >>> m.get_current_player_name()
        'p1'
        >>> m = m.make_move('ll')
        >>> m.get_current_player_name()
        'p2'
        """
        return GameState.get_current_player_name(self)

    def make_move(self, move_to_make: str)-> 'ChopstickState':
        """
        Return a new ChopstickState with move_to_make applied to self.
        >>> m = ChopstickState(True)
        >>> n = m.make_move('ll')
        >>> print(m)
        Player 1: 1-1; Player 2: 1-1
        >>> print(n)
        Player 1: 1-1; Player 2: 2-1
        """
        new = copy.copy(self)
        current_player = new.get_current_player_name()
        if move_to_make == 'll':
            if current_player == 'p1':
                new.p2l = (new.p2l + new.p1l) % 5
            else:
                new.p1l = (new.p1l + new.p2l) % 5
        elif move_to_make == 'lr':
            if current_player == 'p1':
                new.p2r = (new.p2r + new.p1l) % 5
            else:
                new.p1r = (new.p1r + new.p2l) % 5
        elif move_to_make == 'rr':
            if current_player == 'p1':
                new.p2r = (new.p1r + new.p2r) % 5
            else:
                new.p1r = (new.p1r + new.p2r) % 5
        elif move_to_make == 'rl':
            if current_player == 'p1':
                new.p2l = (new.p2l + new.p1r) % 5
            else:
                new.p1l = (new.p1l + new.p2r) % 5
        new._turn += 1
        return new


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
