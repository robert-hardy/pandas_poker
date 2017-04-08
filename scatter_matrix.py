from all_hands_to_scores import score_to_pc
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

df_opponents = pd.concat(
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
df_opponents.columns = df_opponents.columns.get_level_values(0)


if __name__ == '__main__':
    ax = pd.scatter_matrix(df_scores, s=2)
    for i, row in enumerate(ax):
        for j, item in enumerate(row):
            if i != j:
                item.set_xlim(0, 8000)
                item.set_ylim(0, 8000)
    plt.savefig('scatter_matrix.png')

    ax = pd.scatter_matrix(df_opponents, s=2)
    for i, row in enumerate(ax):
        for j, item in enumerate(row):
            if i != j:
                item.set_xlim(0, 8000)
                item.set_ylim(0, 8000)
    plt.savefig('scatter_matrix_opponents.png')

    df_pc = df_scores.applymap(score_to_pc)
    ax = pd.scatter_matrix(df_pc, s=2)
    for i, row in enumerate(ax):
        for j, item in enumerate(row):
            if i != j:
                item.set_xlim(0, 1.0)
                item.set_ylim(0, 1.0)
    plt.savefig('scatter_matrix_of_pc.png')

    df_pc = df_scores.applymap(score_to_pc)
    ax = pd.scatter_matrix(df_pc, s=2)
    for i, row in enumerate(ax):
        for j, item in enumerate(row):
            if i != j:
                item.set_xlim(0, 0.15)
                item.set_ylim(0, 0.15)
    plt.savefig('scatter_matrix_of_pc_zoom.png')
