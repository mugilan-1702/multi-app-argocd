from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Environment variable-இல் இருந்து ENV பெறும்
ENV = os.getenv("APP_ENV", "unknown")

@app.route('/api/hello')
def hello():
    return jsonify({
        "message": f"Hello from Backend!",
        "environment": ENV,   # dev / staging / production
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)