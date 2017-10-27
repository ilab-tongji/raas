from __future__ import absolute_import
from __future__ import print_function
from flask import Flask, send_from_directory,render_template, request, session, redirect, url_for, jsonify
from flask_cors import CORS
from qa import qa_service
import os
from nlp.interpreter import analyse
from distribution import distribute
from nlp.brain import Brain
from flask import g, current_app
from flask_socketio import SocketIO, emit
from tornado.httpserver import HTTPServer


# create 'static' folder
if not os.path.isdir(os.path.join(os.path.dirname(__file__), 'static')):
    os.makedirs(os.path.join(os.path.dirname(__file__), 'static'))


app = Flask(__name__)
CORS(app)


app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='gevent')


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('receive_msg')
def receive_msg(msg):
    emit('server_response',{'data': msg['data']})


cache = {'storyid': None}


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
    print(question)
    # question = request.form['question']
    # print question
    r = Brain().listen(question, cache['storyid'])
    cache['storyid'] = r.get('storyid', None)
    print (cache['storyid'])
    print(r)
    resp = {
        'instructions': {
            'say': r['text']
        }
    }
    socketio.emit(r['intent_type'], r)
    return jsonify(resp)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')