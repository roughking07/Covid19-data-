from django.shortcuts import render
import requests
# Create your views here. https://api.covid19india.org/data.json
def home(request):
    response = requests.get('https://api.covid19india.org/data.json').json()
    labels =[]
    chartdata=[]
    
    for state in response['statewise']:
        labels.append(state['state'])
        chartdata.append(state['confirmed'])

    return render(request,'home.html',{'response':response, 'labels':labels, 'chartdata':chartdata})