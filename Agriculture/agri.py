import pandas as pd 
import numpy as np 
import matplotlib as mp

data=pd.read_csv(r"C:\Users\madhura.anand\Desktop\pybasic\pandasplay\agriiiiiiiiiiiii.csv")
yr=data[['State_Name', 'Area','Crop_Year','Crop']].groupby(['State_Name','Crop'])
for key,item in yr:
    df=yr.get_group(key)
    print(df, "\n\n")
    maxyear=df['Crop_Year'].max()
    print(maxyear)
    print(df.loc[('2001'),'Area'])



