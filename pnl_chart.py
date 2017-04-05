from dataframe_builder import build_dataframe
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random


random.seed(0)
_, _, df = build_dataframe()

df.columns = df.columns.get_level_values(1)
df['win'] = df[1] - df[0]

df.ix[df.win!=0, 'win'] = df.ix[df.win!=0, 'win'] / df.ix[df.win!=0, 'win'].abs()

df[['win']].cumsum().plot()
plt.savefig('1_opponent_pnl.png')
