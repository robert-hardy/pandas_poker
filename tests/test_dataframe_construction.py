import unittest

from deuces import (
    Deck
)
import pandas as pd
import random
random.seed(0)


class TestDFConstruction(unittest.TestCase):
    def setUp(self):
        self.all_cards = [ Deck().draw(5 + 2*2) for x in range(5) ]

    def test_board(self):
        hand = [ (i for i in hand) for hand in self.all_cards ]
        df_board = pd.DataFrame({
            'board': [
                [cards.next() for _ in range(5)]
                for cards in hand
            ]
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
