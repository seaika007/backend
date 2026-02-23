from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO FROM FLASK"

@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    return jsonify({
        "name": data.get("name"),
        "age": data.get("age")
    })

if __name__ == "__main__":
    app.run(port=5000)