from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

input_csv = pd.read_csv('./nishio/tmp.csv')
input_csv2 = pd.read_csv('./nishio/tmp2.csv')
input_csv3 = pd.read_csv('./nishio/change4.csv')
first_column_data = input_csv[input_csv.keys()[12]]
second_column_data = input_csv[input_csv.keys()[7]]

first_column_data2 = input_csv2[input_csv2.keys()[12]]
second_column_data2 = input_csv2[input_csv2.keys()[7]]
first_column_data3 = input_csv3[input_csv3.keys()[12]]
second_column_data3 = input_csv3[input_csv3.keys()[7]]
plt.rcParams["font.size"] = 18
plt.xlabel(input_csv.keys()[12])
plt.ylabel(input_csv.keys()[7])

plt.plot(first_column_data, second_column_data, linestyle='dashed', marker='+', markersize=2)
plt.plot(first_column_data2, second_column_data2, linestyle='solid', marker='v', markersize=2)
#plt.plot(first_column_data3, second_column_data3, linestyle='solid', marker='^')
plt.legend(labels=['threshold 24', 'double-sided'])
plt.title("反転数と時間の関係(重複含む)", fontname="MS Gothic")

plt.show()