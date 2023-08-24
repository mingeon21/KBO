from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render 
import joblib 


YEARS=[str(y) for y in range(2023, 2002, -1)]
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

def loadfile(request):
    template = loader.get_template('status/table.html')
    pitcherInfo=[] 
    f=open('status/data/PitchingStats_2022.tsv')
    for line in f.readlines():
        words=line.split('\t')
        pitcherInfo.append(words)
    context = {
        'pitcherInfo': pitcherInfo
    }
    return HttpResponse(template.render(context, request))

def result(request):
    if request.POST and 'current_year' in request.POST:
        current_year = request.POST['current_year']
    else:
        current_year = '2023'
    if request.POST and 'ip' in request.POST:
        current_ip = request.POST['ip']
    else:
        current_ip = "-1"
    print(current_year)
    eraData, whipData = makeData(current_year)
    era, whip=predict(float(current_ip))
    context = {'eraData': eraData, 'whipData': whipData, 'years': YEARS, 'current_year': current_year, 'current_ip': current_ip, 'era': era, 'whip': whip}
    return render(request, 'result.html', context )

def predict(ip):
    model_era = joblib.load('status/model/kbo_model_ERA.joblib')
    model_whip = joblib.load('status/model/kbo_model_WHIP.joblib')
    predict_era = model_era.predict([[ip]])
    print(predict_era)
    predict_whip = model_whip.predict([[ip]])
    print(predict_whip)
    return (predict_era, predict_whip)




def makeData(year):
    eraData = []
    whipData = []
    f=open('status/data/PitchingStats_'+ year +'.tsv')
    for line in f.readlines() [1:]:
        words=line.rstrip().split('\t')
        ip= stringToFloat(words[10])
        if words[3] == '-' or float(words[3])>50:
            words[3] = '-5'
        if words[-1] == '-' or float(words[-1])>10:
            words[-1] = '-5'
        era = float(words[3])
        whip = float(words[-1])
        eraData.append([ip, era])
        whipData.append([ip,whip])
    return eraData, whipData


