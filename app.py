from flask import Flask,jsonify
from flask import json
import logging

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    data = {"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}
    app.logger.info('Metrics request successfull')

    return jsonify(data)


@app.route("/status")
def status():
    data = {"result":"OK - healthy"}
    app.logger.info('Status request successfull')

    return jsonify(data) 

# @app.route('/status')
# def status():
#     response = app.response_class(
#             response=json.dumps({"result":"OK - healthy"}),
#             status=200,
#             mimetype='application/json'
#     )

#     return response

# @app.route('/metrics')
# def metrics():
#     response = app.response_class(
#             response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
#             status=200,
#             mimetype='application/json'
#     )

#     return response

@app.route("/")
def hello():
    ## log line
    app.logger.info('Main request successfull')

    return "Hello World!"




if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')
