from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def gender_to_numeric(x):
    if x=='Male': return 1
    if x=='Female': return 2

df = pd.read_csv('weight-height.csv')
df['Gender_num']=df['Gender'].apply(gender_to_numeric)
print (df)

X=df[["Height", "Gender_num"]]
y=df["Weight"]

#print (X)
#print (y)

line_fitter = LinearRegression()
line_fitter.fit(X.values.reshape(-1,2), y)

print(line_fitter.predict([[70, 1]]))
print (line_fitter.coef_)
print (line_fitter.intercept_)