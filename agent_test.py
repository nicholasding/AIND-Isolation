"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import random
import isolation
import game_agent
import sample_players

from importlib import reload

verbose = True

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_minimax(self):
        """
        Example
        """
        win = 0
        for _ in range(10):
            if self.play():
                win += 1
        print(win / 10.0)

    def play(self):
        """
        Play a single match
        """
        self.player1 = game_agent.AlphaBetaPlayer(score_fn=sample_players.improved_score)
        self.player2 = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score)
        self.game = isolation.Board(self.player1, self.player2)

        self.game.apply_move(random.choice(self.game.get_legal_moves()))

        if verbose:
            print('Player 1', self.player1)
            print('Player 2', self.player2)
            winner, history, outcome = self.game.play()
            print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
            print(self.game.to_string())
            print("Move history:\n{!s}".format(history))
            return winner == self.player2
        else:
            winner, history, outcome = self.game.play()
            return winner == self.player2


if __name__ == '__main__':
    unittest.main()
