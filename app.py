from flask import Flask, make_response, request, Response
import sys
import os
import subprocess as sp
import datetime

## check upload directory if not exists then crash
UPLOAD_DIR = "./twiml/record/upload"
if not os.path.exists(UPLOAD_DIR):
    print("You can not have three process at the same time.")
    sys.exit('Create the upload dir first:' + UPLOAD_DIR)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/call/cdr", methods=["GET", "POST"])
def call_cdr():
    logging_request(request)
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

@app.route("/pivot/gatherHandler", methods = ["POST", "GET"])
def dtmf_handler():
    logging_request(request)
    data = read_req_body(request)
    forwardExtension = data['Digits']
    print('forwardExtension: ', forwardExtension)

    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
                    <Response>
                    <Say> You are routed to the new extension </Say>
                    <Dial>
                        <Sip>{forwardExtension}@2600hz.com</Sip>
                    </Dial>
                    </Response>'''
    return Response(xml_content, mimetype='application/xml')



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

# for simple action like Say, Play, Hangup
@app.route("/pivot/twiml/<string:action>", methods=["POST", "GET"])
# for complex action like Dial, Record, Gather
@app.route("/pivot/twiml/<string:action>/<string:filename>", methods=["PUT", "GET"])
# for `record` action with uploaded file
# /pivot/twiml/record/upload/call_recording_SaIQOD-sPTqUFK6yFOboZw...mp3 [PUT]
@app.route("/pivot/twiml/<string:action>/upload/<string:recorded_file>", methods=["PUT", "GET"])
def pivot(action, filename=None, recorded_file=None):
    logging_request(request)
    # no `action` and no `recordingUrl` attributes for `record` action
    if request.method == "PUT" and action == "record": 
        data = read_req_body(request)
        fname = "./twiml/" + action + "/upload/" + recorded_file
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
