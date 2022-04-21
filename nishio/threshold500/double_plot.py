from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

input_csv = pd.read_csv('./t11.csv')
input_csv2 = pd.read_csv('./t13.csv')
input_csv3 = pd.read_csv('./t15.csv')
input_csv4 = pd.read_csv('./t17.csv')
input_csv5 = pd.read_csv('./t19.csv')
input_csv6 = pd.read_csv('./t21.csv')
input_csv7 = pd.read_csv('./t23.csv')
input_csv8 = pd.read_csv('./t25.csv')
input_csv9 = pd.read_csv('./t27.csv')
first_column_data = input_csv[input_csv.keys()[12]]
second_column_data = input_csv[input_csv.keys()[7]]
first_column_data2 = input_csv2[input_csv2.keys()[12]]
second_column_data2 = input_csv2[input_csv2.keys()[7]]
first_column_data3 = input_csv3[input_csv3.keys()[12]]
second_column_data3 = input_csv3[input_csv3.keys()[7]]
first_column_data4 = input_csv4[input_csv4.keys()[12]]
second_column_data4 = input_csv4[input_csv4.keys()[7]]
first_column_data5 = input_csv5[input_csv5.keys()[12]]
second_column_data5 = input_csv5[input_csv5.keys()[7]]
first_column_data6 = input_csv6[input_csv6.keys()[12]]
second_column_data6 = input_csv6[input_csv6.keys()[7]]
first_column_data7 = input_csv7[input_csv7.keys()[12]]
second_column_data7 = input_csv7[input_csv7.keys()[7]]
first_column_data8 = input_csv8[input_csv8.keys()[12]]
second_column_data8 = input_csv8[input_csv8.keys()[7]]
first_column_data9 = input_csv9[input_csv9.keys()[12]]
second_column_data9 = input_csv9[input_csv9.keys()[7]]
plt.rcParams["font.size"] = 18
plt.xlabel(input_csv.keys()[12])
plt.ylabel(input_csv.keys()[7])
plt.title("閾値ごとの反転数と時間の関係", fontname="MS Gothic")
plt.plot(first_column_data, second_column_data, linestyle='dashed', marker='o')
plt.plot(first_column_data2, second_column_data2, linestyle='solid', marker='v')
plt.plot(first_column_data3, second_column_data3, linestyle='solid', marker='^')
plt.plot(first_column_data4, second_column_data4, linestyle='solid', marker='^')
plt.plot(first_column_data5, second_column_data5, linestyle='solid', marker='^')
plt.plot(first_column_data6, second_column_data6, linestyle='solid', marker='^')
plt.plot(first_column_data7, second_column_data7, linestyle='solid', marker='^')
plt.plot(first_column_data8, second_column_data8, linestyle='solid', marker='^')
plt.plot(first_column_data9, second_column_data9, linestyle='solid', marker='^')
plt.legend(labels=['11', '13', '15', '17', '19', '21', '23', '25', '27'])
plt.show()