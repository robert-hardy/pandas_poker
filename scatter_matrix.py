from dataframe_builder import build_dataframe
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

_, _, df_scores = build_dataframe()

ax = pd.scatter_matrix(df_scores)
plt.savefig('scatter_matrix.png')
