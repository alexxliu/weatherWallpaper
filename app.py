from flask import Flask, render_template, jsonify, request
from get_weather import getWeather

app = Flask(__name__)

@app.route('/')
def index():
    return """
<div>
"""

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city_name = request.args.get('city_name')
    weather_info = getWeather(city_name)
    return jsonify({"weather_info": weather_info})

if __name__ == '__main__':
    app.run(debug=True)
