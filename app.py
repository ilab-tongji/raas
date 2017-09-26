from __future__ import absolute_import
from __future__ import print_function
from flask import Flask, send_from_directory
from flask_cors import CORS
import os


# create 'static' folder
if not os.path.isdir(os.path.join(os.path.dirname(__file__), 'static')):
    os.makedirs(os.path.join(os.path.dirname(__file__), 'static'))


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/getfile/<string:filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(debug=True)