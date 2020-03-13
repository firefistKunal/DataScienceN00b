import pandas as pd 
import numpy as np
import matplotlib as mp
import sklearn.linear_model as sk
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split

dataset=pd.read_csv(r"C:\Users\madhura.anand\Desktop\pybasic\pandasplay\irisdata.csv")
# print(dataset.head(2))
# print(dataset.shape)
# print(dataset.describe())
# print(dataset.groupby('species').size())
X=dataset.head(75)
y=dataset.head(75)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train)
print("..........................................................................")
print(X_test)
print("..........................................................................")
print(y_train)
print("..........................................................................")
print(y_test)
model=sk.KNeighborsClassifier()
model1=model.fit(X_train,y_train)
print("mmmmmmmmmmmmmmmmooooooooooooooooooooooodddddddddddeeeeeeeeeeeelllllllllllllllllllllll")
print(model1)
predictions=model.predict(X_test)
print("pppppppppppppppprrrrrrrrrrrrrrrrrrrrrreeeeeeeeeeeeeeeeddddictiooooooooooooonnnnnnnnnn")
print(predictions)
print("aaaaaaccccccccccccuuuuuuuuuuuuuuuuurrrrrrrrrrrrrrrraaaaaaaaaaccccccyyyyyyyyyyyyy")
print(accuracy_score(y_test,predictions))