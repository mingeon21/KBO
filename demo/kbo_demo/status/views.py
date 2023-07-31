from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render 

def loadfile(request):
    template = loader.get_template('status/table.html')
    pitcherInfo=[] 
    f=open('status/data/PitchingStats_2023.tsv')
    for line in f.readlines():
        words=line.split('\t')
        pitcherInfo.append(words)
    context = {
        'pitcherInfo': pitcherInfo
    }
    return HttpResponse(template.render(context, request))

def result(request):
    w, era = makeData()
    context = {'w': w, 'era': era}
    return render(request, 'result.html', context )


def makeData():
    era =[] 
    w = []
    f=open('status/data/PitchingStats_2023.tsv')
    for line in f.readlines() [1:]:
        words=line.split('\t')
        w.append(int (words[5]))
        if words[3] == '-':
            words[3] = '200'
        era.append(float(words[3]))
    return w, era 