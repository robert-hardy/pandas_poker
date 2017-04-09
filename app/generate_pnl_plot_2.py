from app.build_dataframe import build_dataframe
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import random
random.seed(0)

df = build_dataframe(1000)

pnl = df[1] - df[0]
pnl.ix[pnl != 0] = pnl / abs(pnl)

pnls = pd.DataFrame(
    pnl.values.reshape(100, 10)
)
cum_pnls = pnls.cumsum()
cum_pnls.plot()
plt.savefig('plots/pnl_plot_2.png')
