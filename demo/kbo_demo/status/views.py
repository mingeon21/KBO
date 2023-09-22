from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render 
import joblib 

YEARS=[str(y) for y in range(2023, 2002, -1)]

STATS_INDEX = {
	'ERA':3,
	'G':4,
	'W':5,
	'L':6,
    'SV':7,
    'HLD':8,
    'WPCT':9,
	'IP':10,
    'H':11,
    'HR':12,
    'BB':13,
    'HBP':14,
    'SO':15,
    'R':16,
    'ER':17,
    'WHIP':18
}


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

    if request.POST and 'current_x' in request.POST:
        current_x = request.POST['current_x']
    else:
        current_x = 'ERA'
    
    if request.POST and 'current_y' in request.POST:
        current_y = request.POST['current_y']
    else:
        current_y = 'IP'

    print(current_year, current_x, current_y)
    plotData, fullData = makeData(current_year, current_x, current_y)
    min_info, max_info = minMaxInfo(plotData, fullData, current_x, current_y)
    context = {
        'plotData': plotData,
        'years': YEARS, 
        'stats_index': STATS_INDEX.keys(),
        'current_year': current_year, 
        'current_x': current_x,
        'current_y': current_y,
        'min_info': min_info,
        'max_info': max_info
        }
    return render(request, 'result.html', context)

def predict(ip):
    model_era = joblib.load('status/model/kbo_model_ERA.joblib')
    model_whip = joblib.load('status/model/kbo_model_WHIP.joblib')
    predict_era = model_era.predict([[ip]])
    print(predict_era)
    predict_whip = model_whip.predict([[ip]])
    print(predict_whip)
    return (predict_era, predict_whip)


def makeData(year, x, y):
    plotData = []
    fullData =[]
    f=open('status/data/PitchingStats_'+ year +'.tsv')
    for line in f.readlines() [1:]:
        words=line.rstrip().split('\t')
        words[10] = stringToFloat(words[10])
        if words[3] == '-' or float(words[3])>50:
            continue
        if words[-1] == '-' or float(words[-1])>10:
            continue
        x_val = words[STATS_INDEX[x]]
        y_val = words[STATS_INDEX[y]]
        if x_val == '-' or y_val =='-':
            continue
        plotData.append([float(x_val), float(y_val)])
        fullData.append(words)
    return plotData, fullData


def minMaxInfo(plotData, fullData, x, y):
    min_index = plotData.index(min(plotData))
    max_index = plotData.index(max(plotData))
    min_info = [
        fullData[min_index][1], 
        fullData[min_index][2], 
        fullData[min_index][STATS_INDEX[x]], 
        fullData[min_index][STATS_INDEX[y]]
    ]
    max_info = [
        fullData[max_index][1], 
        fullData[max_index][2], 
        fullData[max_index][STATS_INDEX[x]], 
        fullData[max_index][STATS_INDEX[y]]
    ]
    return min_info, max_info


def ml(request):
    if request.POST and 'ip' in request.POST:
        current_ip = request.POST['ip']
    else:
        current_ip = '-1'

    era, whip = predict(float(current_ip))
    context = {
        'current_ip': current_ip, 
        'era': era, 
        'whip': whip,
    }
    return render(request, 'ml.html', context)


