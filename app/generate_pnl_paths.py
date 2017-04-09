from app.build_dataframe import build_dataframe

df = build_dataframe(1000)

pnl = df[1] - df[0]
pnl.ix[pnl != 0] = pnl.ix[pnl != 0] / abs(pnl)
pnl = pnl.cumsum()
