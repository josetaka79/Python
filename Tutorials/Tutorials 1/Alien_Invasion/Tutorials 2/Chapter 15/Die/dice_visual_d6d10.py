

import plotly.express as px
from die import Die

# Create a D6 (6-sided die) and a D10 (10-sided die)
die_1 = Die()
die_2 = Die(10)

# Roll the dice 50,000 times and store the results
results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in possible_results]

# Visualize the results
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

# Customize chart layout
fig.update_layout(xaxis_dtick=1)

# Save and display the figure
fig.write_html('dice_visual_d6d10.html')
fig.show()



