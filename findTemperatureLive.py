import requests

def findTemperatureLive(zip_code=None):  
    """Get the current temperature and city name using a weather API."""
    if zip_code:
        # Use a weather API to get the temperature and city name for the given zip code
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={zip_code}")
        data = response.json()
        city_name = data['location']['name']
        temperature = data['current']['temp_f']
        return temperature, city_name
    else:
        # Default to Boston weather
        weather = requests.get("https://www.boston.com/weather").text
        curLoc = weather.find("local-weather__current-info-temp")
        if curLoc != -1:
            degLoc = weather.find("<sup>&deg", curLoc)
            tempLoc = weather.rfind(">", 0, degLoc)
            temperature = weather[tempLoc+1:degLoc]
            return temperature, "Boston"
        else:
            return "N/A", "Boston"

if __name__ == "__main__":
    temp, city = findTemperatureLive()
    print(f"Temperature in {city} is {temp} degrees")
