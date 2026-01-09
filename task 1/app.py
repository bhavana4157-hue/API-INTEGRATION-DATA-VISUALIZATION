from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "79169a0ed7bff51708e55ee648c344d4"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City not provided"})

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": data.get("message", "City not found")})

    return jsonify({
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    })

if __name__ == "__main__":
    app.run(debug=True)
