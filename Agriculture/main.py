import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def cropAreaPerYear(data):

    print(data.index)
    crop=input("\nWhat crop you want?")
    data.loc[crop,:].plot(kind='line', subplots=True) 
    plt.show()
    return 0

def cropShare(data):
    data.loc[:,('Area', 2014)].plot(kind='pie', subplots=True, autopct='%1.1f%%') 
    plt.show()
    return 0



original=pd.read_csv('apy.csv')
print(original['State_Name'].unique())
state=input("Which state you want info on?? ")
state_data=original[original['State_Name']==state] 

data=state_data.groupby(['Crop_Year','Crop'])['Area'].agg(np.sum).reset_index().pivot(index='Crop', columns='Crop_Year')
choice=int(input("Enter 1 to get share of crops in state as pie chart\nor Enter 2 to get change in crop area through years\n"))
if choice==1:
    cropAreaPerYear(data)
elif choice==2:
    cropShare(data)
else:
    print("\nYou chose poorly\n")


# print(data.drop('Rice').columns)
# data.drop('Rice').sort_values(by=('Area', 2014)).plot.barh()
# plt.show()


# plt.bar(data.loc['Rice',:].reset_index()['Crop_Year'], data.loc['Rice',:].reset_index()['Rice'])
# plt.show()

