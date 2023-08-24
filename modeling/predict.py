from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib


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

def checkForMinus(str):
    print(str)
    if '-' in str :
        return 100
    else:
        return float(str)         

def train(input_file_name, output_file_name, x_name, y_name):
    df = pd.read_csv(input_file_name, sep="\t")
    X = df[x_name].apply(stringToFloat)
    y = df[y_name].apply(checkForMinus)
    print(X)
    print(y)

    line_fitter = LinearRegression()
    line_fitter.fit(X.values.reshape(-1,1), y)

    joblib.dump(line_fitter, output_file_name) 


def main():
    x_name = 'IP'
    y_name = 'WHIP'
    train('data/PitchingStats_2023.tsv', f'./kbo_model_{y_name}.joblib', x_name, y_name)
    model = joblib.load('./kbo_model.joblib')
    predict_val = model.predict([[5], [6]])
    print(predict_val)

main()