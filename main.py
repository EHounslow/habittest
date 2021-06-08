import flask

from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return flask.render_template("index.html")
       
    if request.method == 'POST':
        # A multidict containing POST data
        return flask.render_template("name.html", message=request.form['name-input'])

       
app.run(host='0.0.0.0', port=81)