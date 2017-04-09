from app.build_dataframe import build_dataframe
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

df = build_dataframe(1000)
pd.scatter_matrix(df)
plt.savefig('plots/scatter_matrix_2.png')
