import pandas as pd

with open('nishio/doub.csv') as f:
    print(f.read())
# name,age,state,point
# Alice,24,NY,64
# Bob,42,CA,92
# Charlie,18,CA,70
# Dave,68,TX,70
# Ellen,24,CA,88
# Frank,30,NY,57

df = pd.read_csv('nishio/doub.csv')

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

#print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57


df.loc[df['iteration'] < 100, 'iteration'] = 0
print(df)
df.to_csv("nishio/change.csv")