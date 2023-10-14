import requests
import json

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]

        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = "7fde9519194430304188222841efecc2"  # 여기에 발급받은 API 키를 넣으세요.
    
    get_weather(city_name, api_key)
