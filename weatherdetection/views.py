from django.shortcuts import render
import json
import urllib.request as urllibRequest

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        request_url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=fa5d11f033eda552e91921718fa9bc3b'
        print(request_url)
        res = urllibRequest.urlopen(request_url).read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ', ' +  str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'K',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }
    else:
        data = {}
        city = ''
    return render(request, 'index.html', {'city':city, 'data':data}) 