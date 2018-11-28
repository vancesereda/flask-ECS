# services/users/project/__init__.py



from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig') # new



@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
    'status': 'success',
    'message': 'pong!'
    })


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        "response":"Hello World!"
    })