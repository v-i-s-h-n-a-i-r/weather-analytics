from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! from Flask"


# Simple notifications route
@app.route('/notifications')
def notifications():
    mock_notification = {
        "message": "You have a new weather alert!",
        "type": "alert"
    }
    return jsonify(mock_notification)

if __name__ == "__main__":
    app.run(debug=True)
