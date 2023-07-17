from pickle import NONE
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


def stringToFloat(ip_str):
    ip=0
    words=ip_str.split(" ")
    if '/' in words[0]:
        if words[0][0] =='1':
            ip=ip+0.33
        else:
            ip=ip+0.66
    else:
        ip=ip+float(words[0])

    if len(words)>1:
        if words[1][0] =='1':
            ip=ip+0.33
        else:
            ip=ip+0.66
    return (ip)
            


df = pd.read_csv('data/PitchingStats_2023.tsv', sep="\t")

print (df)

X=[x for x in df["W"]]
X=np.array(X)
y = [[stringToFloat(y) for y in df["IP"]]]
y=np.array(y)
print(y)
print(X)


line_fitter = LinearRegression()
line_fitter.fit(X.reshape(1,-1), y)

print(line_fitter.predict([10]))
print (line_fitter.coef_)
print (line_fitter.intercept_)