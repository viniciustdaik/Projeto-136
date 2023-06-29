from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success",
    }), 200


@app.route("/star")
def planet():
    name = request.args.get("name")

    if name != None:
        star_data = next(item for item in data if
                         str(item["name"]).lower().strip() == str(name).lower().strip())
        return jsonify({
            "data": star_data,
            "message": "success",
        }), 200
    else:
        return jsonify({
            "data": data,
            "message": "success",
        }), 200


if __name__ == "__main__":
    app.run()
