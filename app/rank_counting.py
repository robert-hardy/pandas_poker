from collections import Counter
from datetime import datetime
from deuces import (
    Deck,
    Evaluator
)
import random
random.seed(1)


print 'Generating the hands.'
print datetime.now()
hands = [ Deck().draw(5) for _ in range(1000000) ]

e = Evaluator()
print 'Scoring them.'
print datetime.now()
scores = [ e.evaluate(x, []) for x in hands ]
ranks = [ e.get_rank_class(s) for s in scores ]
rank_strings = [ e.class_to_string(r) for r in ranks ]

print 'Counting them.'
print datetime.now()
c = Counter(rank_strings)
for i in c.most_common(10):
    print i
