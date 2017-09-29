from __future__ import absolute_import
from __future__ import print_function
from flask import Flask, send_from_directory,render_template, request, session, redirect, url_for, jsonify
from flask_cors import CORS
from qa import qa_service
import os


# create 'static' folder
if not os.path.isdir(os.path.join(os.path.dirname(__file__), 'static')):
    os.makedirs(os.path.join(os.path.dirname(__file__), 'static'))


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return render_template('homepage.html')


@app.route('/getfile/<string:filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory('static', filename)

@app.route('/service/qa',methods=['POST'])
def get_answer():
    mock = {'type': 'weather', 'slots': {'city': 'shanghai','day':0}}
    answer = qa_service.get_answer(mock['type'],mock['slots'])
    return render_template('homepage.html',answer=answer)



if __name__ == '__main__':
    app.run(debug=True)