import requests
from apikey import API_KEY

lat, lon = 41.3552444, 60.7817031
part = "daily"
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_KEY}"
res = requests.get(url)
print(res.json())
