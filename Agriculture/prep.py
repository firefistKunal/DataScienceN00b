import pandas as pd
import numpy as np

class crop:
    def __init__(self, name):
        self.name=name
        

    def __init__(self, raw):
        raw_data=raw

class district():
    name=""
    area=""
    def __init__(self, raw):
        self.in_data=raw

class state():

    def __init__(self, name):
        self.name=name
        self.raw=pd.read_csv("apy.csv")
        self.data=self.raw[self.raw["State_Name"]==self.name]
    def totalArea(self, year):
        self.area=self.data.groupby(['Crop_Year'])['Area'].agg(np.sum)
        return state.area[year]
    
    def totalProduction(self, year):
        self.area=self.data.groupby(['Crop_Year'])['Production'].agg(np.sum)
        return state.area[year]

    def efficiency(self, year):
        return (self.totalProduction(year)/self.totalArea(year))*100


state=state("Chhattisgarh")
print(state.totalProduction(2014))
print(state.efficiency(2014))
