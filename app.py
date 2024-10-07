from flask import Flask, jsonify 
from flask_cors import CORS


import requests

app = Flask(__name__) 
CORS(app)

# Weather API configuration
API_KEY = 'd9cd7eff12ec4da6973173943240610'  # Weather API Key
CITY = 'Hyderabad'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

@app.route('/weather', methods=['GET'])
def get_weather():
    # Fetch weather data from the external API
    response = requests.get(f'{BASE_URL}?key={API_KEY}&q={CITY}')
    
    if response.status_code == 200:
        weather_data = response.json()
        # Return a JSON response with relevant weather details
        return jsonify({
            "city": weather_data['location']['name'],
            "temperature": weather_data['current']['temp_c'],
            "condition": weather_data['current']['condition']['text'],
            "humidity": weather_data['current']['humidity']
        })
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
