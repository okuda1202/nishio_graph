import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = pd.read_csv("./nishio/normalrowhammer.csv")
data.describe()
plt.rcParams["font.size"] = 18
plt.scatter(data[' former flip'], data[' later flip'])

plt.title("前半後半の反転数", fontname="MS Gothic")
plt.ylabel('later')
plt.xlabel('fomer')
plt.show()