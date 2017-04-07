from all_hands_to_scores import score_to_pc
from deuces import Deck, Evaluator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import random


random.seed(0)
e = Evaluator()
hands = [ Deck().draw(5) for _ in range(10000) ]
scores = [ e.evaluate(x) for x in hands ]
pcs = [ score_to_pc(x) for x in scores ]
s = pd.Series(pcs)
s = s.sort_values().reset_index(drop=True)
s.plot()
plt.figsave('test_score_to_pc.png')
