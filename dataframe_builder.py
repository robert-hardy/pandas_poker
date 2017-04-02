from deuces import (
    Deck,
    Card,
    Evaluator
)
import pandas as pd
import random


random.seed(0)
hand = [ Deck() for _ in range(5) ]
df_board = pd.DataFrame({
    'board': [ deck.draw(5) for deck in hand ]
})

players = [
    pd.DataFrame({
        'player': [ deck.draw(2) for deck in hand ]
    })
    for _ in range(2)
]
df_players = pd.concat(players, axis=1, keys=range(2))
df_players = df_players.swaplevel(0, 1, axis=1)
