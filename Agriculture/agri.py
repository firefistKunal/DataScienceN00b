import pandas as pd 
import numpy as np 
import matplotlib as mp

data=pd.read_csv(r"C:\Users\madhura.anand\Desktop\pybasic\pandasplay\agriiiiiiiiiiiii.csv")
yr=data[['State_Name', 'Area','Crop_Year','Crop']].groupby(['State_Name','Crop'])
for key,item in yr:
        print(yr.get_group(key), "\n\n")
print(".......................................................................................................................................")
for key,item in yr:
    print(yr.get_group(key), "\n\n")
