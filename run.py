from deuces import (
    Deck,
    Card,
    Evaluator
)
import pandas as pd
import random

random.seed(0)

all_cards = [ Deck().draw(9) for x in range(1000) ]
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

def who_won(x, y):
    if x == y:
        return 0
    if x > y:
        return 1
    return 2

df['winner'] = df.apply(lambda x: who_won(x['score1'], x['score2']), axis=1)


# Was the game fair?
draws, one, two = df.groupby('winner').count().iloc[:, 0].values

print "Draws: {0}\nPlayer one: {1}\nPlayer two: {2}\n".format(draws, one, two)
