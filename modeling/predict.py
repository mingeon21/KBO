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
            

def train(input_file_name, output_file_name):
    df = pd.read_csv(input_file_name, sep="\t")
    X = df['W']
    df['IP'] = df['IP'].apply(stringToFloat)
    y = df['IP']
    print(X)
    print(y)

    line_fitter = LinearRegression()
    line_fitter.fit(X.values.reshape(-1,1), y)

    joblib.dump(line_fitter, output_file_name) 


def main():
    train('PitchingStats_2023.tsv', 'kbo_model.joblib')
    model = joblib.load('kbo_model.joblib')
    predict_val = model.predict([[5], [6]])
    print(predict_val)


main()