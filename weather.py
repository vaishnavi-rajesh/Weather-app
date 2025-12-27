import requests

API_KEY = "b402b54208d0280b407dd762833e7e9e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition.capitalize()}")

    elif response.status_code == 401:
        print("Invalid API key or key not activated yet. Please wait a few minutes.")

    elif response.status_code == 404:
        print("City not found. Check the city name and try again.")

    else:
        print("Something went wrong. Please try again later.")


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
