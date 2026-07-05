import requests


def get_weather(city: str):

    # Step 1: Get coordinates
    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    geo_response = requests.get(geo_url, timeout=10).json()

    if "results" not in geo_response:
        return {"error": f"City '{city}' not found"}

    location = geo_response["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    # Step 2: Get weather
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    weather = requests.get(weather_url, timeout=10).json()

    current = weather["current"]

    return {
        "city": city,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
    }

