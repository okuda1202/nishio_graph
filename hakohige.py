import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.read_csv("./nishio/normaledit.csv")
plt.boxplot((df1[' former flip'], df1[' later flip'], df1[' sum flip']), labels=['former', 'later', 'sum flips'])

plt.title('boxplot')
plt.show()