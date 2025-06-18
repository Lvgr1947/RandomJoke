from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin for local testing

@app.route('/joke')
def joke():
    return jsonify({"joke": "Why don't scientists trust atoms? Because they make up everything!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)