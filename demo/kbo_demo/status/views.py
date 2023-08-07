from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render 

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
    eraData, whipData = makeData()
    context = {'eraData': eraData, 'whipData': whipData}
    return render(request, 'result.html', context )


def makeData():
    eraData = []
    whipData = []
    f=open('status/data/PitchingStats_2022.tsv')
    for line in f.readlines() [1:]:
        words=line.split('\t')
        ip= stringToFloat(words[10])
        if words[3] == '-' or float(words[3])>50:
            words[3] = '-5'
        era = float(words[3])
        whip = float(words[-1])
        eraData.append([ip, era])
        whipData.append([ip,whip])
    return eraData, whipData


