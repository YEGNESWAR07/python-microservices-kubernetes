from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Service 2!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)