from dataframe_builder import build_dataframe
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import random

random.seed(0)
_, _, df_scores = build_dataframe(
    nb_hands=1000,
    nb_players=5
)

df_scores.columns = df_scores.columns.get_level_values(1)
ax = pd.scatter_matrix(df_scores, s=2)

for i, row in enumerate(ax):
    for j, item in enumerate(row):
        if i != j:
            item.set_xlim(0, 8000)
            item.set_ylim(0, 8000)
plt.savefig('scatter_matrix.png')
