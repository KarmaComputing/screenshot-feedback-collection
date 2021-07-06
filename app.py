from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def collect_feedback():
    comment = request.json["comment"]
    screenshot = request.json["screenshot"]
    msg = {
        "msg": "feedback received",
        "comment": comment,
        "screenshot": screenshot,
    }  # noqa: E501
    return msg
