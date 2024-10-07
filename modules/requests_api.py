import requests
import json
#
API_KEY = "3ec853fb4f9e9deead9292a202be9e5b"
#
CITY_NAME = "Dnipro"
#
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#
response = requests.get(URL)
#
if response.status_code == 200:
    #
    data = json.loads(response.content)
    #
    print(json.dumps(data, indent= 4))