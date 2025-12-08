import numpy as np
import pandas as pd
from collections import Counter
x = np.linspace(-5, 5, 1000)

mean = 0
sigma = 1

y = (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.e ** -((x - mean) ** 2) / (2 * sigma ** 2)

# Or a bit more nicely laid out...

scale_term = (1 / np.sqrt(2 * np.pi * sigma ** 2))
exponent_term = ((x - mean) ** 2) / (2 * sigma ** 2)
y = scale_term * np.e ** -exponent_term

from matplotlib import pyplot as plt
plt.plot(x, y, "-");

from scipy import stats

n = stats.norm(0, 1)

# Generate 10 random variates from this distribution
n.rvs(10)

# note that Counter isn't very helpful here. It is *highly* likely that all counts will be 1
# regardless of how many values you generate. In fact, it's nearly impossible to get the same value twice.
results = n.rvs(10)

Counter(results)

# Histograms work better here

import altair as alt
alt.renderers.enable('default')

normal_values = pd.DataFrame({"value": n.rvs(5000)})

alt.Chart(normal_values).mark_bar().encode(
    alt.X("value", bin=alt.Bin(maxbins=100)),
    y='count()',
    color=alt.value('#287E1E'),
)

if not alt.data_transformers.active == 'json':  # Check json isn't already active
    import os
    # Make a temp folder to put these json files in - Altair creates a lot of them!
    dataset_temp_name = 'altair-temp-data/'
    if not os.path.exists(dataset_temp_name):
        # if the folder doesn't exist, create it
        os.mkdir(dataset_temp_name)
    # Tell Altair to temporary save datasets it needs to that folder
    alt.data_transformers.enable('json', prefix=dataset_temp_name)

normal_values = pd.DataFrame({"value": n.rvs(100000)})

alt.Chart(normal_values).mark_bar().encode(
    alt.X("value", bin=alt.Bin(maxbins=100)),
    y='count()',
)