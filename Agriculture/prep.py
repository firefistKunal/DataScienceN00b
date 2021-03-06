import pandas as pd
import numpy as np

class crop:
    def __init__(self, name):
        self.name=name
        self.raw=pd.read_csv("apy.csv")
        self.data=self.raw[self.raw["Crop"]==self.name]

    def nationalArea(self, year):
        self.area=self.data.groupby(['Crop_Year'])['Area'].agg(np.sum)
        return self.area[year]
    
    def nationalProduction(self, year):
        self.production=self.data.groupby(['Crop_Year'])['Production'].agg(np.sum)
        return self.production[year]

    def efficiency(self, year):
        return (self.nationalProduction(year)/self.nationalArea(year))*100

class state():

    def __init__(self, name):
        self.name=name
        self.raw=pd.read_csv("apy.csv")
        self.data=self.raw[self.raw["State_Name"]==self.name]

    def totalArea(self, year):
        self.area = self.data.groupby(['Crop_Year'])['Area'].agg(np.sum)
        return self.area[year]
    
    def totalProduction(self, year):
        self.area=self.data.groupby(['Crop_Year'])['Production'].agg(np.sum)
        return self.area[year]

    def efficiency(self, year):
        return (self.totalProduction(year)/self.totalArea(year))*100


rice=crop("Rice")
print(rice.efficiency(2014))
