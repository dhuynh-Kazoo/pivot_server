from flask import Flask, make_response, send_file, render_template
import os
import subprocess as sp

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#@app.route("/pivot/twiml/<string:action_file>")
#def pivot(action_file):
#    file_path = os.path.join(os.getcwd() + "/twiml/", action_file)
#    response = make_response(send_file(file_path))
#    # content-type: text/xml;charset=UTF-8   
#    response.headers["content-type"] = "text/xml;charset=UTF-8"	
#    # file_path = "twiml/dial.php"
#    return response

@app.route("/pivot/twiml/<string:action_file>")
def pivot(action_file):
    file_path = os.path.join(os.getcwd() + "/twiml/", action_file)
    out = sp.run(["php", file_path], stdout=sp.PIPE)
    response = make_response(out.stdout)
    response.headers["content-type"] = "text/xml;charset=UTF-8"
    return response
