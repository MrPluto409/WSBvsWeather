import requests,json


def getWeather():
  weatherURL = "https://api.openweathermap.org/data/2.5/weather?"
  APIKey = "355c78809c3b8837bda20915474303d0"
  City = "Minneapolis"
  URL = weatherURL + "q=" + City + "&APPID=" + APIKey
  responseNumber = requests.get(URL)
  data = responseNumber.json()
  main = data["main"]
  print(main)
    
getWeather()
