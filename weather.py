import requests

def get_weather(city):
    API_KEY = '92b39585c2593956f888e5305ba6c8e8'  # Replace with your OpenWeatherMap API key
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # for Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"\n🌤️ Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather}")
    else:
        print("⚠️  City not found or API error!")

if __name__ == "__main__":
    city = input("📝 Enter city name: ")
    get_weather(city)
