from __future__ import absolute_import
from __future__ import print_function
from flask import Flask, send_from_directory,render_template, request, session, redirect, url_for, jsonify
from flask_cors import CORS
from qa import qa_service
import os
from nlp.interpreter import analyse
from distribution import distribute


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


@app.route('/service/qa', methods=['POST'])
def get_answer():
    mock = {'type': 'weather', 'slots': {'city': 'shanghai','day':0}}
    answer = qa_service.get_answer(mock['type'],mock['slots'])
    return render_template('homepage.html',answer=answer)


@app.route("/ask", methods=['POST'])
def ask():
    """

     accept type: json
     accept format: json
     {
        "question": xxx
        ...
     }

     return type : json
     return format:
        {
            "instructions": {
                "say": xxx,
                "move": xxx,
                ...
            }
        }
    """
    data = request.json
    question = data['question']
    # question = request.form['question']
    # print question
    inner = analyse(question)
    service = distribute(inn=inner)
    answer = service(inner)
    resp = {
        'instructions': {
            'say': answer
        }
    }
    return jsonify(resp)


if __name__ == '__main__':
    app.run(port=5000, debug=True)