from deuces import (
    Deck,
    Evaluator
)
import pandas as pd


def build_dataframe(nb_hands=100, nb_players=2):
    decks = [ Deck() for _ in range(nb_hands) ]

    df_board = pd.DataFrame({
        'board': [ deck.draw(5) for deck in decks ]
    })

    df_players = pd.concat(
        [
            pd.DataFrame({
                'player': [ deck.draw(2) for deck in decks ]
            })
            for _ in range(nb_players)
        ],
        axis=1,
        keys=range(nb_players)
    )
    df_players = df_players.swaplevel(0, 1, axis=1)

    evaluator = Evaluator()
    df_scores = pd.concat(
        [
            df_board.join(df_players.xs(i, level=1, axis=1)).apply(
                lambda x: evaluator.evaluate(x['board'], x['player']),
                axis=1
            ).to_frame('score')
            for i in df_players.columns.get_level_values(1)
        ],
        axis=1,
        keys=df_players.columns.get_level_values(1)
    )
    df_scores = df_scores.swaplevel(0, 1, axis=1)

    return df_board, df_players, df_scores
