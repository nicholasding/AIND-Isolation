"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_minimax(self):
        self.player1 = game_agent.MinimaxPlayer(4)
        self.player2 = game_agent.MinimaxPlayer(2)
        self.game = isolation.Board(self.player1, self.player2)

        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        print(self.game.to_string())

        # print(self.player1.get_move(self.game, lambda: 100.0))

        print('Player 1', self.player1)
        print('Player 2', self.player2)
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))


if __name__ == '__main__':
    unittest.main()
