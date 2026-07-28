from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
request_count = 0


@app.before_request
def count_requests():
    global request_count
    request_count += 1


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Ghaymah SRE API",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "ghaymah-sre-api",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/stats")
def stats():
    return jsonify({
        "requests": request_count
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
