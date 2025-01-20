from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib
import os
import math

def stringToFloat(ip_str):
    ip=0
    words=ip_str.split(" ")
    if '/' in words[0]:
        if words[0][0] =='1':
            ip = ip+0.33
        else:
            ip = ip+0.66
    else:
        ip = ip + float(words[0])

    if len(words)>1:
        if words[1][0] =='1':
            ip = ip + 0.33
        else:
            ip = ip + 0.66
    return ip

def checkForMinus(_str):
    print(_str)
    if isinstance(_str, str) and '-' in _str :
        return 100
    elif isinstance(_str, float) and math.isnan(_str):
        return 50
    else:
        return float(_str)         

def train(input_dir, output_file_name, x_name, y_name):
    files = os.listdir(input_dir)
    df_all_years = pd.DataFrame()

    for file in files:
        input_file_name = f'{input_dir}/{file}'
        print(input_file_name)
        df = pd.read_csv(input_file_name, sep="\t")
        df_all_years = pd.concat([df_all_years, df])

    X = df_all_years[x_name].apply(stringToFloat) 
    y = df_all_years[y_name].apply(checkForMinus)
    print(X)
    print(y)

    line_fitter = LinearRegression()
    line_fitter.fit(X.values.reshape(-1,1), y)

    joblib.dump(line_fitter, output_file_name) 


def main():
    x_name = 'IP'
    y_name = 'ERA'
    train('data', f'./kbo_model_{y_name}.joblib', x_name, y_name)
    model = joblib.load('./kbo_model.joblib')
    predict_val = model.predict([[5], [6]])
    print(predict_val)

main()