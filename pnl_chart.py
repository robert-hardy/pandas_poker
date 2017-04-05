from dataframe_builder import build_dataframe
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
import pandas as pd


random.seed(0)
_, _, df_scores = build_dataframe(nb_players=5)
df_scores.columns = df_scores.columns.get_level_values(1)

df = pd.concat(
    [
        df_scores[[0]],
        df_scores[[1]].min(axis=1),
        df_scores[[1, 2]].min(axis=1),
        df_scores[[1, 2, 3]].min(axis=1),
        df_scores[[1, 2, 3, 4]].min(axis=1)
    ],
    axis = 1,
    keys = range(5)
)
df.columns = df.columns.get_level_values(0)

df['win'] = df[2] - df[0]

df.ix[df.win!=0, 'win'] = df.ix[df.win!=0, 'win'] / df.ix[df.win!=0, 'win'].abs()

df[['win']].cumsum().plot()
plt.savefig('1_opponent_pnl.png')
