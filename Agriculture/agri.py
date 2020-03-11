import pandas as pd 
import numpy as np 
import matplotlib as mp

data=pd.read_csv("apy.csv")
# yr=data[['State_Name', 'Area','Crop_Year','Crop']].groupby(['State_Name','Crop'])
# for key,item in yr:
#     df=yr.get_group(key)
#     print(df, "\n\n")
#     maxyear=df['Crop_Year'].max()
#     print(maxyear)
#     # print(df.loc[('maxyear'),'Area'])

yr=data[data['State_Name']=='Chhattisgarh'] #take data of a state, any state

yr=yr.groupby(['Crop_Year'])['Area'].agg(np.sum) #group it by year and add by area
print(yr) #print the output

