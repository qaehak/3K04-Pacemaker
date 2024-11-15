# Test how to plot data

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#create data frame
df = pd.DataFrame({'x': [0,1,2,3],
                   'y': [0,1,2,3]})

#set up seaborn
sns.set()

#set axis
ax = sns.lineplot(data=df, x='x',y='y')

plt.title("Test")

#display plot
plt.show()