from deuces import (
    Deck,
    Evaluator
)
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


deck = Deck().draw(52)
e = Evaluator()
all_hands = [ list(x) for x in combinations(deck, 5) ]
all_scores = [ e.evaluate(x, []) for x in all_hands ]

s = pd.Series(all_scores)
s = s.sort_values().reset_index(drop=True)
df = s.to_frame('score')

LENGTH = len(df)
df['pc'] = (1.0 + df.index)/LENGTH
#df.remove_duplicates('score', take_last=True)
