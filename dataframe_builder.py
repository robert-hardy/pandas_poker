from deuces import (
    Deck,
    Card,
    Evaluator
)
from itertools import islice
import pandas as pd
import random


random.seed(0)
all_cards = [ Deck().draw(5 + 2*2) for x in range(5) ]
hand = [ (i for i in hand) for hand in all_cards ]
df_board = pd.DataFrame({
    'board': [
        [cards.next() for _ in range(5)]
        for cards in hand
    ]
})

s = pd.Series(all_cards)
players = []
for i in range(2):
    i_start = 5 + 2*i
    i_end = i_start + 2
    df_player = (s.apply(
        lambda x: list(islice(x, i_start, i_end))
    )).to_frame('player')
    players.append(df_player)
df_players = pd.concat(players, axis=1, keys=range(2))
