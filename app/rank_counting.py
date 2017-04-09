from collections import Counter
from deuces import (
    Deck,
    Evaluator
)
import random
random.seed(1)


hands = [ Deck().draw(5) for _ in range(10000) ]

e = Evaluator()
scores = [ e.evaluate(x, []) for x in hands ]
ranks = [ e.get_rank_class(s) for s in scores ]
rank_strings = [ e.class_to_string(r) for r in ranks ]

c = Counter(rank_strings)
for i in c.most_common(10):
    print i
