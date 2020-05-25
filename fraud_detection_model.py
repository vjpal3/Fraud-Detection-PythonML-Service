from flask import Flask, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/api/fraud-detection")
def index():
    return "Welcome to Python Server"

@app.route("/api/fraud-detection/health.json")
def health():
    return jsonify({"status": "UP"}), 200



if __name__ == "__main__":
    app.run(host='localhost', port='8090')
