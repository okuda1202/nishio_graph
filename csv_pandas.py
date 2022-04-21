import pandas as pd

with open('data/src/sample_pandas_normal.csv') as f:
    print(f.read())
# name,age,state,point
# Alice,24,NY,64
# Bob,42,CA,92
# Charlie,18,CA,70
# Dave,68,TX,70
# Ellen,24,CA,88
# Frank,30,NY,57

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

