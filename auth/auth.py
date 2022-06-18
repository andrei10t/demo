import logging
import basicauth
import json
from flask import request
USER = "admin"
PASS = "admin"

from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def result():
    authorization = request.headers.get('Authorization')
    logging.info(request)
    if authorization is not None and "Basic " in authorization:
        username, passwd = basicauth.decode(authorization)
        print(username, passwd)
        if username is USER and passwd is PASS:
            print("right credentials")
            response = json.dump({'good'})
            return response, 201
        else:
            print("wrong credentials")
            response = json.dump({'not good'})
            return response, 403
    response = json.dump({'really bad'})
    return response, 403


if __name__ == "__main__":
    logging.info("service started")
    app.run(debug=True, host='0.0.0.0', port= 5001)