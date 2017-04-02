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
    all_cards = [ Deck().draw(5 + 2*nb_players) for x in range(10000) ]
    df = pd.DataFrame({'all': all_cards})
    df['board'] = df['all'].apply(lambda x: x[:5])
    for i in range(nb_players):
        i_start = 5 + 2*i
        i_end = i_start + 2
        df['player{0}'.format(i+1)] = df['all'].apply(lambda x: list(islice(x, i_start, i_end)))
    del df['all']
    return df

df = deal_cards(3)
evaluator = Evaluator()
df['score1'] = df.apply(lambda x: evaluator.evaluate(x['board'], x['player1']), axis=1)
df['score2'] = df.apply(lambda x: evaluator.evaluate(x['board'], x['player2']), axis=1)
df['score3'] = df.apply(lambda x: evaluator.evaluate(x['board'], x['player3']), axis=1)

df['score_min23'] = df[['score2', 'score3']].min(axis=1)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

ax = df.plot.scatter(x='score1', y='score2')
fig = ax.get_figure()
fig.savefig('2_hand_scatter_full.png')

df.plot.scatter(x='score1', y='score_min23', color='Red', marker='+', ax=ax)
fig.savefig('3_hand_scatter_full.png')

hands = df[(df.score1 > 3325) & (df.score2 > 3325) & (df.score3 > 3325)]
