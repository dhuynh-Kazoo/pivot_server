from flask import Flask, make_response, send_file, render_template, request
import os
import subprocess as sp
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/call/cdr", methods=["GET", "POST"])
def call_cdr():
    logging_request(request)
    return '', 200

# recordin POST with action attribute
# @app.route("/pivot/twiml/record", methods=["GET", "POST"])
# def record_for_action():
#     logging_request(request)

#     return '', 200

# /pivot/twiml/record/upload/call_recording_b6i_QqcnsKFNhxgifX9nbA...mp3
# http://192.168.1.16:5000/pivot/kazoo/record/upload/call_recording_98QjCmrcLae1ho1UvakHTg...mp3
@app.route("/pivot/<string:format>/record/upload/<string:recorded_file>", methods = ['POST', 'PUT'])
def record_upload(format, recorded_file):
    logging_request(request)
    record_path = "./" + format + "/record/upload/"
    data = read_req_body(request)
    fname = os.path.join(record_path + recorded_file)
    fname = fname.replace('...', '.')
    with open(fname, "wb") as file:
        file.write(data)
    return '', 200

# http://192.168.1.16:5000/pivot/twiml/dial/conference/wait
@app.route("/pivot/twiml/dial/conference/wait", methods=["GET", "POST"])
def wait_conference():
    logging_request(request)
    return '', 200

@app.route("/pivot/gather", methods = ["POST", "GET"])
def collect_dtmf():
    logging_request(request)
    return '', 200    

@app.route("/pivot/kazoo/<string:filename>", methods=["GET", "POST"])
def kazoo_pivot(filename=None):
    file_path = os.path.join(os.getcwd() + "/kazoo/", filename)
    if os.path.exists(file_path):
        out = sp.run(["php", file_path], stdout=sp.PIPE)
        response = make_response(out.stdout)
        response.headers["Content-Type"] = "application/json;charset=UTF-8"
        return response
    else:
        return "FILE NOT FOUND", 404
   

# for simple action like Say, Play, Hangup
@app.route("/pivot/twiml/<string:action>", methods=["POST", "GET"])
# for complex action like Dial, Record, Gather
@app.route("/pivot/twiml/<string:action>/<string:filename>", methods=["PUT", "GET"])
# for `record` action with uploaded file
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
            print(action, filename)
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
