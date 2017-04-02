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
df_all = pd.DataFrame({'all': all_cards})
df_board = pd.DataFrame(df_all['all'].apply(lambda x: x[:5]))
df_board.columns = ['board']
players = []
for i in range(2):
    i_start = 5 + 2*i
    i_end = i_start + 2
    df_player = pd.DataFrame((df_all['all'].apply(lambda x: list(islice(x,
        i_start, i_end)))))
    df_player.columns = ['player']
    players.append(df_player)
df_players = pd.concat(players, axis=1, keys=range(2))
