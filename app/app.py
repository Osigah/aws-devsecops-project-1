from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "AWS DevSecOps Project 1 is running",
        "app": "flask-demo"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "dev"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)