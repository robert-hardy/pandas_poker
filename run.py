from deuces import (
    Deck,
    Card,
    Evaluator
)
import pandas as pd

all_cards = [ Deck().draw(9) for x in range(10) ]
df = pd.DataFrame({'all': all_cards})

df['board'] = df['all'].apply(lambda x: x[:5])
df['player1'] = df['all'].apply(lambda x: x[5:7])
df['player2'] = df['all'].apply(lambda x: x[7:9])

evaluator = Evaluator()
df['score1'] = df.apply(lambda x: evaluator.evaluate(x['board'], x['player1']), axis=1)
df['score2'] = df.apply(lambda x: evaluator.evaluate(x['board'], x['player2']), axis=1)
df['class1'] = df['score1'].apply(lambda x: evaluator.get_rank_class(x))
df['class2'] = df['score2'].apply(lambda x: evaluator.get_rank_class(x))
df['class1_string'] = df['class1'].apply(lambda x: evaluator.class_to_string(x))
df['class2_string'] = df['class2'].apply(lambda x: evaluator.class_to_string(x))
