import pandas as pd 
import numpy as np
import csv
from datetime import datetime as dt

data=pd.read_csv('covid-19(india).csv')

def date():

    return dt.now().strftime("%d-%m-%Y")

def time():
    if dt.now().strftime("%p")=="AM":
        return "Morning"
    else:
        return "Evening"

def addInfection():
    State=input("State??\t")
    Place=input("Place??\t")
    Date=date()
    Time=time()
    Infected=int(input("How many Infected??\t"))
    Total_Infected=data["Total_Infected"].iloc[-1]+Infected

    return [State, Place, Date, Time, Infected, Total_Infected]


while int(input("1 to Add\n0 to close")):
    dt=data.groupby(['State'])['Infected'].agg(np.sum).to_frame()
    print(dt.sort_values(by=['Infected'], ascending=False))
    data.loc[len(data)]=addInfection()
    print(data)
    data.to_csv('covid-19(india).csv', index=False)
    


