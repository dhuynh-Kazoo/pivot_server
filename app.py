from flask import Flask, make_response, send_file, render_template, request
import os
import subprocess as sp

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# http://localhost:5000/pivot/record/upload/call_recording_HiFzH3wlY9NwcWAw-J_W6Q...mp3
@app.route("/pivot/record/upload/<string:recorded_file>", methods = ['POST', 'PUT'])
def record_upload(recorded_file):
    print("=========================================")
    print("Request queries: ", request.args.to_dict())
    print("Request Content-Type: ", request.content_type)
    print("Request body: ", request.files)
    print("=========================================")

    data = request.get_data()
    fname = os.path.join("./recorded_calls/" + recorded_file)
    with open(fname, "wb") as file:
        file.write(data)
    return '', 200

@app.route("/pivot/gather", methods = ["POST", "GET"])
def collect_dtmf():
    print("=========================================")
    print("Request queries: ", request.args.to_dict())
    json_data = request.form or request.get_json()
    data = dict(json_data)
    print("Request body: ", data)
    print("=========================================")
    return '', 200    


@app.route("/pivot/twiml/<string:action_file>")
def pivot(action_file):
    file_path = os.path.join(os.getcwd() + "/twiml/", action_file)
    if os.path.exists(file_path):
        out = sp.run(["php", file_path], stdout=sp.PIPE)
        response = make_response(out.stdout)
        response.headers["content-type"] = "text/xml;charset=UTF-8"
        return response
    else:
        return "FILE NOT FOUND", 404

