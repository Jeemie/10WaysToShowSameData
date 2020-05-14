import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cars-sample.csv', index_col=0)

colors = ['#A3A500',
          '#E76BF3',
          '#F8766D',
          '#00BF7D',
          '#00B0F6']

sns.lmplot(x='Weight', y='MPG', data=df,
           fit_reg=False,
           hue='Manufacturer',
            palette = colors)

plt.show()