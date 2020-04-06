import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn import metrics as m

data=pd.read_csv(r"C:\Users\madhura.anand\Desktop\pybasic\malicious-and-benign-websites\dataset.csv")
data1=data.drop(['Type','CHARSET','SERVER','WHOIS_COUNTRY','WHOIS_STATEPRO','WHOIS_REGDATE','WHOIS_UPDATED_DATE','URL'],axis=1)
target1=data['Type']
#imp = SimpleImputer(strategy="most_frequent")
data2=pd.DataFrame(data1).fillna(0)
X_train, X_test, y_train, y_test = train_test_split(data2,target1 , test_size=0.2, random_state=0)

regressor = LogisticRegression()
regressor.fit(X_train, y_train)
y_pred=regressor.predict(X_test)
cnf_matrix = m.confusion_matrix(y_test, y_pred)
print(cnf_matrix)