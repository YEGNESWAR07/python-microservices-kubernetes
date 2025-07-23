from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Service 1!"})

@app.route('/call-service2')
def call_service2():
    response = requests.get("http://service2:5000")
    return jsonify({
        "service1": "Hello from Service 1!",
        "service2_response": response.json()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)