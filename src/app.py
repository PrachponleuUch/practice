from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route("/api/v1/welcome", methods=["GET"])
def welcome():
    return jsonify({
        "message": "Welcome to the Flask API!!!!!!",
        "hostname": socket.gethostname(),
        "deployed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
@app.route("/api/v1/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}, 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
