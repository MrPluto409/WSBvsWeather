import requests,json

def getWeather():
  weatherURL = "https://api.openweathermap.org/data/2.5/weather?"
  APIKey = "355c78809c3b8837bda20915474303d0"
  lattitude = "44.98891411861488"
  longitidue = "-93.22727597285993"
  URL = weatherURL + "lat=" + lattitude + "&lon=" + longitidue  + "&APPID=" + APIKey + "&units=imperial" 
  responseNumber = requests.get(URL)
  data = responseNumber.json()
  wind = data["wind"]
  windSpeed = wind["speed"]
  windStock = round(windSpeed)
  return windStock
  
    
getWeather()
