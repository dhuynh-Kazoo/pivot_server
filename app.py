from flask import Flask, make_response, send_file, render_template, request
import os
import subprocess as sp
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# http://localhost:5000/pivot/record/upload/call_recording_HiFzH3wlY9NwcWAw-J_W6Q...mp3
@app.route("/pivot/record/upload/<string:recorded_file>", methods = ['POST', 'PUT'])
def record_upload(recorded_file):
    logging_request(request)

    data = request.get_data()
    fname = os.path.join("./recorded_calls/" + recorded_file)
    with open(fname, "wb") as file:
        file.write(data)
    return '', 200

@app.route("/pivot/gather", methods = ["POST", "GET"])
def collect_dtmf():
    logging_request(request)
    return '', 200    


@app.route("/pivot/twiml/<string:action_file>", methods=["POST", "GET"])
@app.route("/pivot/twiml/<string:action_file>/<string:recorded_file>", methods=["PUT"])
def pivot(action_file, recorded_file=None):
    logging_request(request)
    if request.method == "PUT": # no `action` and no `recordingUrl` attributes for `record` action
        return '', 200
    if request.method == "POST": # no `action` attribute
        return '', 200
    else: # GET method
        file_path = os.path.join(os.getcwd() + "/twiml/", action_file)
        if os.path.exists(file_path):
            out = sp.run(["php", file_path], stdout=sp.PIPE)
            response = make_response(out.stdout)
            response.headers["content-type"] = "text/xml;charset=UTF-8"
            return response
        else:
            return "FILE NOT FOUND", 404


def logging_request(request):
    now = datetime.datetime.now()
    url = request.base_url
    json_data = request.form or request.get_json()
    if json_data:
        data = dict(json_data)
    else:
        data = request.get_data()
    
    print("\n\n")
    print("====================================")
    print("[{}] - url {} {}".format(now, request.method, url))
    print("[{}] - queries: {}".format(now, request.args.to_dict()))
    print("[{}] - url {}".format(now, data))
