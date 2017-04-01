from collections import Counter
from deuces import (
    Deck,
    Card,
    Evaluator
)
from itertools import islice
import pandas as pd
import random


random.seed(0)
def deal_cards(nb_players=2):
    all_cards = [ Deck().draw(5 + 2*nb_players) for x in range(1000) ]
    df = pd.DataFrame({'all': all_cards})
    df['board'] = df['all'].apply(lambda x: x[:5])
    for i in range(nb_players):
        i_start = 5 + 2*i
        i_end = i_start + 2
        df['player{0}'.format(i+1)] = df['all'].apply(lambda x: list(islice(x, i_start, i_end)))
    del df['all']
    return df

df = deal_cards()
evaluator = Evaluator()
df['score1'] = df.apply(lambda x: evaluator.evaluate(x['board'], x['player1']), axis=1)
df['score2'] = df.apply(lambda x: evaluator.evaluate(x['board'], x['player2']), axis=1)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

ax = df.plot()
fig = ax.get_figure()
fig.savefig('foo.png')
