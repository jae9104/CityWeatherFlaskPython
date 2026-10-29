import os
import ssl
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen
import json

import certifi
from dotenv import load_dotenv
from flask import Flask, render_template, request


load_dotenv()

app = Flask(__name__)
WEATHER_URL = "https://api.weatherapi.com/v1/current.json"
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


def clothing_advice(temperature: float) -> str:
    if temperature < 5:
        return "Wear a warm coat, gloves, and a hat."
    if temperature < 15:
        return "Wear a jacket or sweater and long trousers."
    if temperature < 25:
        return "A light jacket or long-sleeve top should be comfortable."
    return "Wear light, breathable clothes and consider sunglasses."


def get_weather(city: str) -> dict:
    api_key = os.getenv("WEATHER_API_KEY") or os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("WEATHER_API_KEY is not configured.")

    query = urlencode(
        {
            "q": city,
            "key": api_key,
        }
    )

    with urlopen(
        f"{WEATHER_URL}?{query}", timeout=10, context=SSL_CONTEXT
    ) as response:
        data = json.load(response)

    temperature = data["current"]["temp_c"]
    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": round(temperature),
        "description": data["current"]["condition"]["text"],
        "advice": clothing_advice(temperature),
    }


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error = "Please enter a city."
        else:
            try:
                weather = get_weather(city)
            except (RuntimeError, ValueError) as exc:
                error = str(exc)

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
