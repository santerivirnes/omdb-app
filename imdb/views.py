from django.shortcuts import render

# Create your views here.

import json, requests
baseurl = "http://www.omdbapi.com/?t="
apikey = "33980cae"


def index(request):
    return render(request, "input.html")

def search(request):

    name = request.POST['name']
    

    response = requests.get(baseurl + name + "&apikey=" + apikey)


    if response.status_code == 200:
        res = json.loads(response.text)
        return render(request, "result.html", {"result": res})
    else:
        res = "Bad request!"
        return render(request, "result.html", {"result": res})
        

