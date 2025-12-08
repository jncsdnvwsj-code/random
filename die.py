import random

possible_states = [1, 2, 3, 4, 5, 6]

random.choice(possible_states)

NUM_TRIALS = 100000

results = [random.choice(possible_states) for i in range(NUM_TRIALS)]

from collections import Counter
counts = Counter(results)
counts

import altair as alt
alt.renderers.enable('default')

import pandas as pd

die_rolls = pd.DataFrame({
    'state': possible_states,
    'count': [counts.get(state, 0) for state in possible_states]
})

print(die_rolls)

alt.Chart(die_rolls).mark_bar().encode(
    x='state:O',
    y='count'
)