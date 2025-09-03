from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! from Flask"


# Simple weather API endpoint
@app.route('/weather')
def weather():
    mock_weather = {
        "location": "New York",
        "temperature": 22,
        "condition": "Sunny"
    }
    return jsonify(mock_weather)

if __name__ == "__main__":
    app.run(debug=True)
