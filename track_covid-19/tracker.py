import pandas as pd 
import numpy as np
import csv
from datetime import datetime as dt, timedelta as td

data=pd.read_csv('covid-19(India).csv')

# def date():

#     return dt.now().strftime("%d-%m-%Y")
def date():
    day=dt.now()-td(1)
    return day.strftime("%d-%m-%Y")

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
    Infected=infected(State)
    Total_Infected=data["Total_Infected"].iloc[-1]+Infected

    return [State, Place, Date, Time, Infected, Total_Infected]

def infected(state):
    df=data.groupby(['State'])['Infected'].agg(np.sum).reset_index()
    state_total=df[df['State']==state].iloc[0]['Infected']
    
    return int(input("How many Total Infected??\t"))-state_total


while int(input("1 to Add\n0 to close")):
    df=data.groupby(['State'])['Infected'].agg(np.sum).to_frame()
    print(df.sort_values(by=['Infected'], ascending=False))
    data.loc[len(data)]=addInfection()
    print(data)
    data.to_csv('covid-19(india).csv', index=False)
    


