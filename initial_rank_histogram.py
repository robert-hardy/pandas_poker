from collections import Counter
from deuces import (
    Deck,
    Evaluator
)

all_cards = [ Deck().draw(5) for x in range(10000) ]
vals = [ evaluator.evaluate(x, []) for x in all_cards ]
ranks = [ ( evaluator.get_rank_class(v),
    evaluator.class_to_string(evaluator.get_rank_class(v)) ) for v in vals ]
c = Counter(ranks)
c.most_common(10)
