from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)


@app.route("/")
def Index():
    return jsonify({
        "data": data,
        "message": "Success..."
    }), 200


@app.route("/planet")
def Planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "Sucess"
    }), 200


if __name__ == "__main__":
    app.run()
