from django.shortcuts import render,HttpResponse
import requests
# Create your views here.

def index(request):
    #return HttpResponse('<h1>My Application</h1>')
    result=None
    data=True
    globalsummary=None
    countries=None
    while(data):
        try:
            url='https://api.covid19api.com/summary'
            result=requests.get(url) 
            json=result.json()
            globalsummary=json['Global']
            countries=json['Countries']
            data=False
        except:
            data=True



    return render(request,'index.html',{'globalsummary':globalsummary,'countries':countries})

def country(request,country):
    return HttpResponse('Inside custom APi')