from deuces import Deck, Evaluator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


def build_dataframe(nb_hands):
    decks = [ Deck() for _ in range(nb_hands) ]
    boards = [ deck.draw(5) for deck in decks ]
    player1 = [ deck.draw(2) for deck in decks ]
    player2 = [ deck.draw(2) for deck in decks ]

    e = Evaluator()
    scores = [
        (e.evaluate(b, p1), e.evaluate(b, p2))
        for (b, p1, p2) in zip(boards, player1, player2)
    ]

    df = pd.DataFrame(scores)
    return df
