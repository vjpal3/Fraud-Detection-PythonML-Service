from flask import Flask, jsonify
import fraud_detection

app = Flask(__name__)

@app.route("/api/fraud-detection")
def index():
    return "Welcome to Python Server"

@app.route("/api/fraud-detection/health.json")
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/api/fraud-detection/model")
def get_model():
    result = fraud_detection.train_model()
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host='localhost', port='8090')