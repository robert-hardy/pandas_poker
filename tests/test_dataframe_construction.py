import unittest

from deuces import (
    Deck,
    Evaluator
)
import pandas as pd
import random


class TestDFConstruction(unittest.TestCase):
    def test_board(self):
        random.seed(0)
        hand = [ Deck() for _ in range(5) ]
        df_board = pd.DataFrame({
            'board': [ deck.draw(5) for deck in hand ]
        })
        expected = [
            [[81922, 33560861, 139523, 16783383, 147715]],
            [[16783383, 4212241, 295429, 69634, 81922]],
            [[266757, 1082379, 134236965, 557831, 16787479]],
            [[33564957, 8423187, 1065995, 33589533, 98306]],
            [[16795671, 529159, 135427, 16783383, 266757]]
        ]
        self.assertEqual(
            df_board.values.tolist(),
            expected
        )

    def test_draws_are_consistent(self):
        random.seed(0)
        hand = [ Deck() for _ in range(5) ]
        df_all = pd.DataFrame({
            'all': [ deck.draw(9) for deck in hand ]
        })
        expected = [
            [[81922, 33560861, 139523, 16783383, 147715, 69634, 164099, 1053707, 16795671]],
            [[16783383, 4212241, 295429, 69634, 81922, 73730, 134236965, 8394515, 557831]],
            [[266757, 1082379, 134236965, 557831, 16787479, 67127839, 529159, 134253349, 1053707]],
            [[33564957, 8423187, 1065995, 33589533, 98306, 268471337, 2114829, 16812055, 67119647]],
            [[16795671, 529159, 135427, 16783383, 266757, 2106637, 279045, 8423187, 8394515]]
        ]
        self.assertEqual(
            df_all.values.tolist(),
            expected
        )

        random.seed(0)
        hand = [ Deck() for _ in range(5) ]
        df_board = pd.DataFrame({
            'board': [ deck.draw(5) for deck in hand ]
        })
        expected = [
            [[81922, 33560861, 139523, 16783383, 147715]],
            [[16783383, 4212241, 295429, 69634, 81922]],
            [[266757, 1082379, 134236965, 557831, 16787479]],
            [[33564957, 8423187, 1065995, 33589533, 98306]],
            [[16795671, 529159, 135427, 16783383, 266757]]
        ]
        self.assertEqual(
            df_board.values.tolist(),
            expected
        )

class TestScoring(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        hand = [ Deck() for _ in range(5) ]
        self.df_board = pd.DataFrame({
            'board': [ deck.draw(5) for deck in hand ]
        })

        players = [
            pd.DataFrame({
                'player': [ deck.draw(2) for deck in hand ]
            })
            for _ in range(2)
        ]
        df_players = pd.concat(players, axis=1, keys=range(2))
        self.df_players = df_players.swaplevel(0, 1, axis=1)

    def test_no_warning_on_join(self):
        player0 = self.df_players.xs(0, level=1, axis=1)
        self.df_board.join(player0)
