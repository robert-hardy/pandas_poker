import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

equiv_classes = pd.read_csv(
    'equivalence_classes.csv',
    sep=',',
    header=None,
    names=[
        'value',
        '5_cards',
        '6_cards',
        '7_cards',
        '8_cards',
        'sample',
        'abbrev',
        'description'
    ]
)

if __name__ == '__main__':
    df = equiv_classes[['value', '5_cards']].set_index('value')
    df.plot()
    plt.savefig('equiv_classes.png')
