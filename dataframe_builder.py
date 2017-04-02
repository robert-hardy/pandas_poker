from deuces import (
    Deck,
    Evaluator
)
import pandas as pd
import random

NB_HANDS = 10000
NB_PLAYERS = 3

random.seed(0)
hand = [ Deck() for _ in range(NB_HANDS) ]
df_board = pd.DataFrame({
    'board': [ deck.draw(5) for deck in hand ]
})

players = [
    pd.DataFrame({
        'player': [ deck.draw(2) for deck in hand ]
    })
    for _ in range(NB_PLAYERS)
]
df_players = pd.concat(players, axis=1, keys=range(NB_PLAYERS))
df_players = df_players.swaplevel(0, 1, axis=1)

evaluator = Evaluator()
df_scores = pd.concat([
    df_board.join(df_players.xs(i, level=1, axis=1)).apply(
        lambda x: evaluator.evaluate(x['board'], x['player']),
        axis=1
    ).to_frame('score')
    for i in df_players.columns.get_level_values(1)
], axis=1, keys=range(NB_PLAYERS))
df_scores = df_scores.swaplevel(0, 1, axis=1)
