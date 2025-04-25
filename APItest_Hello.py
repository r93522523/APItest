from flask import Flask, jsonify, request
import os

app = Flask(__name__)

AUTH_TOKEN = os.getenv("API_TOKEN", "default_token")

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, world!'})

@app.route('/echo', methods=['POST'])
def echo():
    auth_header = request.headers.get('Authorization')    
    if auth_header != f"Bearer {AUTH_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    return jsonify({'you_sent': data})

if __name__ == '__main__':
    app.run(debug=True)
