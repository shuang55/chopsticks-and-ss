"""a chopsticks Game module - a subclass of GameState"""
from typing import Any
from game import Game
from chopstickstate import ChopstickState


class ChopsticksGame(Game):
    """
    A class to play chopsticks - is a subclass of (extends) class Game
    """
    def __init__(self, p1_turn: bool) -> None:
        """
        Create a new chopsticksGame, with first player p1 if
        p1_turn is true
        >>> m = ChopsticksGame(True)
        >>> print(m)
        Player 1: 1-1; Player 2: 1-1
        """
        self.current_state = ChopstickState(p1_turn)

    def __eq__(self, other: Any)->bool:
        """Return whether ChopsticksGame self is equal to ChopsticksGame other
        >>> m = ChopsticksGame(True)
        >>> n = 8
        >>> m == n
        False
        """
        return Game.__eq__(self, other)

    def __str__(self) -> str:
        """return a string representation of Game self, which
        prints the current GameState
        >>> m = ChopsticksGame(True)
        >>> print(m)
        Player 1: 1-1; Player 2: 1-1
        """
        return self.current_state.__str__()

    def is_over(self, state: ChopstickState) -> bool:
        """Return whether Game self is over
        >>> m = ChopsticksGame(True)
        >>> m.is_over(m.current_state)
        False
        """
        return (state.p1l == 0 and state.p1r == 0) or \
               (state.p2l == 0 and state.p2r == 0)

    def get_instructions(self) -> str:
        """
        return the instructions for Game self
        >>> m = ChopsticksGame(True)
        >>> m.get_instructions()[:7] == 'Players'
        True
        """
        return ('Players take turns adding the values of one ' +
                'of their hands to one of their opponents' +
                ' (modulo 5). A hand with a total of 5 (or 0; modulo 5)' +
                ' is considered dead. ' +
                'The first person to have two dead hands is the loser')

    def is_winner(self, player: str) -> bool:
        """
        Return whether player is a winner in Game Self
        >>> m = ChopsticksGame(True)
        >>> m.is_winner('p1')
        False
        """
        if player == 'p1':
            return self.current_state.p2l == 0 and self.current_state.p2r == 0
        elif player == 'p2':
            return self.current_state.p1l == 0 and self.current_state.p1r == 0
        return False

    def str_to_move(self, move: str) -> str:
        """
        Return the move to be made based on the str move.
        move must be a syntactically correct move, that is
        one of ll, rr, rl, or lr
        >>> m  = ChopsticksGame(True)
        >>> m.str_to_move('ll')
        'll'
        """
        return move


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
