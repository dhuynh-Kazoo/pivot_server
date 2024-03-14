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

    data = read_req_body(request)
    fname = os.path.join("./record/calls/" + recorded_file)
    with open(fname, "wb") as file:
        file.write(data)
    return '', 200

@app.route("/pivot/gather", methods = ["POST", "GET"])
def collect_dtmf():
    logging_request(request)
    return '', 200    


# for simple action like Say, Play, Hangup
@app.route("/pivot/twiml/<string:action>", methods=["POST", "GET"])
@app.route("/pivot/twiml/<string:action>/<string:filename>", methods=["PUT", "GET"])
@app.route("/pivot/twiml/<string:action>/<string:filename>/<string:recorded_file>", methods=["PUT", "GET"])
def pivot(action, filename=None, recorded_file=None):
    logging_request(request)
    # no `action` and no `recordingUrl` attributes for `record` action
    if request.method == "PUT" and action == "record": 
        data = read_req_body(request)
        fname = "./twiml/" + action + "/calls/" + recorded_file
        with open(fname, "wb") as file:
            file.write(data)
        return '', 200
    
    elif request.method == "POST": # no `action` attribute
        return '', 200
    
    else: # GET method
        if action and filename:
            file_path = os.path.join(os.getcwd() + "/twiml/" + action, filename)
        else:
            file_path = os.path.join(os.getcwd() + "/twiml/", action)

        if os.path.exists(file_path):
            out = sp.run(["php", file_path], stdout=sp.PIPE)
            response = make_response(out.stdout)
            response.headers["content-type"] = "text/xml;charset=UTF-8"
            return response
        else:
            return "FILE NOT FOUND", 404

def read_req_body(request):
    json_data = request.form or request.get_json()
    if json_data:
        data = dict(json_data)
    else:
        data = request.get_data()
    return data    
    
def logging_request(request):
    now = datetime.datetime.now()
    url = request.base_url
    json_data = request.form or request.get_json()
    data = read_req_body(request)
    
    print("\n\n")
    print("====================================")
    print("[{}] - url {} {}".format(now, request.method, url))
    print("[{}] - queries: {}".format(now, request.args.to_dict()))
    print("[{}] - url {}".format(now, data))
