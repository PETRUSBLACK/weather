from django.shortcuts import render
import json
import urllib.request 

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.api-ninjas.com/v1/weather?city=city').read()
        json_data = json.loads(res)
    else:
        city = ''
    return render(request, 'index.html', {'city' : city}) 