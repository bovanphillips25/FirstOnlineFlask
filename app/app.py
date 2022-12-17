"""A simple flask web app"""
from flask import Flask, render_template
from controllers.index_controller import IndexController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    form = '<h1>Make a QR Code<h1><form method="POST" action="/"> \
           <label for="qrurl">QR URL:</label><br> \
           <input type="text" id="qrurl" name="qrurl" value="https://www.njit.edu/"><br>\
           <input type="submit" value="Submit"> \
           </form>'
    return IndexController.get(), form
