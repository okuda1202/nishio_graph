import pandas as pd

df = pd.read_csv('nishio/normaledit.csv')

print(type(df))


for index, data in df.iterrows():
    #print(data[4], data[10])
    if (data[4] < 1):
        #data[10] -= data[9]
        #print(df.loc[index, ' searching time'])
        df.loc[index, ' searching time'] = (data[10] - data[9])
        df.loc[index, ' sum flip'] = df.loc[index, ' former flip']
        
    if(index > 0):
        df.loc[index, ' entire time'] = (df.loc[index, ' searching time'] + df.loc[index, ' sum getting time'])
        df.loc[index, ' entire time'] += df.loc[index-1, ' entire time']
        df.loc[index, ' sum flip'] += df.loc[index-1, ' sum flip']
    else:
        df.loc[index, ' entire time'] = (data[10] + data[3])

    
    

df.to_csv("nishio/tmp2.csv")
#print(df)
