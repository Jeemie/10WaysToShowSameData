import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D

# index_col makes it so it skips the first
cardata = pd.read_csv("cars-sample.csv", index_col=0)

figure, ax = plt.subplots()

colors = {'bmw': '#F8766D',
          'ford': '#A3A500',
          'honda': '#00BF7D',
          'mercedes': '#00B0F6',
          'toyota': '#E76BF3'}
ax.scatter(cardata['Weight'], cardata['MPG'],
           c=cardata['Manufacturer'].apply(lambda x: colors[x]),
           s=(cardata['Weight'] / 300) ** 2,
           alpha=0.5
           )

ax.set_xlabel('Weight')
ax.set_ylabel('MPG')
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
legendplot = [Line2D([0], [0], marker='o', color='#F8766D', label='bmw', markersize=5),
              Line2D([0], [0], marker='o', color='#A3A500', label='ford', markersize=5),
              Line2D([0], [0], marker='o', color='#00BF7D', label='honda', markersize=5),
              Line2D([0], [0], marker='o', color='#00B0F6', label='mercedes', markersize=5),
              Line2D([0], [0], marker='o', color='#E76BF3', label='toyota', markersize=5),
              ]
plt.legend(handles=legendplot)
plt.show()
# print(manufacturer)
