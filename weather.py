import requests

def get_weather(city_name):
    API_KEY = "27486d6d35df68371381a3e121acf47e" 
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # so we get temperature in Celsius
    }
    
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found! Please check the spelling.")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)

