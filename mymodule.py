from urllib.request import urlopen
import json

api_key = "xxxxxxx"

def get_weather(city):
  sock = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key)
  
  result = sock.read()
  sock.close()
  weather = json.loads(result)
  return weather["main"]["temp"] - 273.15
  
if __name__ == "__main__":
  degrees = get_weather("OSLO")
  print("Weather in Oslo is %.2f degrees Celsius" % degrees)
