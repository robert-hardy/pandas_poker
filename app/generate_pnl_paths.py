from app.build_dataframe import build_dataframe
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = build_dataframe(1000)

pnl = df[1] - df[0]
pnl.ix[pnl != 0] = pnl / abs(pnl)
pnl = pnl.cumsum()

pnl.plot()
plt.savefig('plots/pnl_plot_1.png')
