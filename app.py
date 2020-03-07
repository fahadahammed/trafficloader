#  Project TrafficLoader is developed by Fahad Ahammed on 3/7/20, 11:12 AM.
#
#  Last modified at 3/7/20, 11:10 AM.
#
#  Github: fahadahammed
#  Email: obak.krondon@gmail.com
#
#  Copyright (c) 2020. All rights reserved.

from flask import Flask, request
import os

app = Flask(__name__)

ENV = os.getenv('ENV', 'prod')  # two env: 1: dev, 2: prod and default is prod

APPLICATION_NAME = f"TrafficLoader_Application-{ENV}"
FILE_NAME_TO_SAVE_DATA = f"data-{APPLICATION_NAME}.txt"


def save_to_file(content):
    try:
        with open(FILE_NAME_TO_SAVE_DATA, "a") as file:
            file.write(str(content) + "\n")
            file.close()
    except Exception as e:
        return e


@app.route('/', methods=["GET"])
def hello():
    return f"Hello from {APPLICATION_NAME}"


@app.route('/save', methods=["POST"])
def hello_save():
    to_save = request.json  # { "message": "Hello..." }
    save_to_file(content=to_save["message"] + f" From {APPLICATION_NAME}")
    return f"Saving in {APPLICATION_NAME}"


if __name__ == "__main__":
    app.secret_key = b'_5#y__RO__4Q8z\n\xec]/'
    app.config["ENV"] = ENV
    if ENV == "dev":
        app.run(host="0.0.0.0", port=15002, debug=True)
    else:
        app.run(host="0.0.0.0", port=15001)
