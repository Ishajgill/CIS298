import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# Tell Flask where to find the static folder
app = Flask(__name__, static_folder="static", static_url_path="/static")
# OpenWeatherMap API Key (Replace with your actual key)
OPENWEATHER_API_KEY = "your_api_key_here"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code != 200:
            return jsonify({"error": data.get("message", "Error fetching data")}), response.status_code

        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
        }

        return jsonify(weather_info)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
