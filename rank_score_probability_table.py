from deuces import (
    Deck,
    Evaluator
)
from itertools import combinations
import pandas as pd


deck = Deck().draw(52)
e = Evaluator()
all_hands = [ list(x) for x in combinations(deck, 5) ]
all_scores = [ e.evaluate(x, []) for x in all_hands ]
all_ranks = [ e.get_rank_class(x) for x in all_scores ]

df_all = pd.DataFrame({
    'score': all_scores,
    'rank': all_ranks
})
df = df_all.groupby('rank').agg({'rank': 'count', 'score': [min, max]})
df.columns = df.columns.get_level_values(1)
df['width'] = df['max'] - df['min'] + 1
df['ratio'] = df['count'] / df['width']
