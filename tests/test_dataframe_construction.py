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
        self.assertEqual(len(df_board), len(self.all_cards))
        self.assertEqual(
            df_board.iloc[0].values.tolist()[0],
            self.all_cards[0][:5]
        )
